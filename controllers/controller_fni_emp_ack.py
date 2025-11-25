from odoo import models, fields, api, tools, _
from odoo.exceptions import UserError, ValidationError, RedirectWarning, AccessDenied, AccessError, CacheMiss, MissingError
import logging

from odoo import http
from odoo.http import request
from odoo.addons.survey.controllers.main import Survey as SurveyController

_logger = logging.getLogger(__name__)


class FnEmpAckSurveyController(SurveyController):
    """Route HR Emp Ack certificates through the hr_emp_ack_report action
    (portrait A4), leave all other surveys (incl. Firenor) on the native flow.
    """

    @http.route('/survey/certification/<string:answer_token>',
                type='http', auth='public', website=True)
    def survey_get_certification(self, answer_token, **post):
        try:
            user_input = request.env['survey.user_input'].sudo().search(
                [('access_token', '=', answer_token)],
                limit=1,
            )
            if not user_input:
                # Let core controller handle errors / redirects
                return super().survey_get_certification(answer_token, **post)

            survey = user_input.survey_id

            # Only intercept HR Emp Ack surveys
            if survey.certification_report_layout != 'fni-ack_o-ack':
                return super().survey_get_certification(answer_token, **post)

            # Use your custom report with its own paperformat_hr_emp_ack
            report = request.env.ref('fn_academy.hr_emp_ack_report').sudo()
            pdf_content, _ = report._render_qweb_pdf([user_input.id])

        except Exception as exc:
            _logger.exception("HR Emp Ack certificate generation failed: %s", exc)
            # Fallback to default behavior if anything goes wrong
            return super().survey_get_certification(answer_token, **post)
        else:
            filename = "Acknowledgement - %s - %s.pdf" % (
                user_input.partner_id.name or survey.title,
                (user_input.create_date or survey.write_date).strftime('%d-%b-%Y'),
            )
            headers = [
                ('Content-Type', 'application/pdf'),
                ('Content-Length', len(pdf_content)),
                ('Content-Disposition', http.content_disposition(filename)),
            ]
            return request.make_response(pdf_content, headers=headers)
        finally:
            # nothing special, hook kept for consistency / future logging
            _logger.debug("survey_get_certification processed for token %s", answer_token)


    @http.route('/survey/<model("survey.survey"):survey>/certification_preview',
                type='http', auth='user', website=True)
    def certification_preview(self, survey, **post):
        try:
            if survey.certification_report_layout != 'fni-ack_o-ack':
                return super().certification_preview(survey, **post)

            # Pick any successful attempt for preview (or your own logic)
            user_input = request.env['survey.user_input'].sudo().search(
                [('survey_id', '=', survey.id),
                 ('state', '=', 'done')],
                limit=1,
            )
            if not user_input:
                # If no attempts yet, just fall back to default preview
                return super().certification_preview(survey, **post)

            report = request.env.ref('fn_academy.hr_emp_ack_report').sudo()
            pdf_content, _ = report._render_qweb_pdf([user_input.id])

        except Exception as exc:
            _logger.exception("HR Emp Ack preview failed: %s", exc)
            return super().certification_preview(survey, **post)
        else:
            headers = [
                ('Content-Type', 'application/pdf'),
                ('Content-Length', len(pdf_content)),
            ]
            return request.make_response(pdf_content, headers=headers)
        finally:
            _logger.debug("certification_preview processed for survey %s", survey.id)

