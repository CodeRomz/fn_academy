from odoo import http
from odoo.http import request
import logging

_logger = logging.getLogger(__name__)

class SurveyCertificateController(http.Controller):
    @http.route(['/fna/certification/<int:user_input_id>'], type='http', auth='public', website=True)
    def view_certificate(self, user_input_id, **kwargs):
        """
        Render the certificate page for the given user_input_id.
        """
        _logger.info(f"Attempting to fetch user input with ID: {user_input_id}")
        # Fetch the survey response using sudo() to bypass security restrictions
        user_input = request.env['survey.user_input'].sudo().browse(user_input_id)
        if not user_input.exists():
            _logger.warning(f"User input with ID {user_input_id} not found.")
            return request.not_found()

        _logger.info(f"Successfully fetched user input: {user_input}")
        # Prepare values for rendering
        values = {
            'docs': user_input,
            'share_url': f"{request.httprequest.host_url}fna/certification/{user_input_id}",
        }

        # Log the rendering action
        _logger.info(f"Rendering certification for user input ID {user_input_id}")

        return request.render('survey.certification_report_view', values)


class SurveyCertificateSharingController(http.Controller):
    @http.route(['/fna/certification/share/<int:user_input_id>'], type='http', auth='public', website=True)
    def share_certificate(self, user_input_id, **kwargs):
        """
        Render a simplified version of the certificate page for social sharing.
        This view includes Open Graph tags in the head for platforms like LinkedIn.
        """
        _logger.info(f"Attempting to fetch user input for sharing with ID: {user_input_id}")

        # Fetch the survey response using sudo() to bypass security restrictions
        user_input = request.env['survey.user_input'].sudo().browse(user_input_id)
        if not user_input.exists():
            _logger.warning(f"User input with ID {user_input_id} not found.")
            return request.not_found()

        _logger.info(f"Successfully fetched user input for sharing: {user_input}")

        # Prepare meta tag information for Open Graph
        og_title = "Certification of Achievement - Firenor Academy"
        og_description = f"Congratulations to {user_input.partner_id.name or user_input.email} for earning the Certification of Achievement in the {user_input.survey_id.display_name} program!"
        og_image_url = f"https://{request.httprequest.host}/fn_academy/static/img/firenor-one_seagreen.png"
        og_url = f"{request.httprequest.host_url}fna/certification/share/{user_input_id}"

        # Prepare values for rendering, including Open Graph metadata
        values = {
            'user_input': user_input,
            'og_title': og_title,
            'og_description': og_description,
            'og_image_url': og_image_url,
            'og_url': og_url,
        }

        # Log the rendering action
        _logger.info(f"Rendering sharing certification for user input ID {user_input_id}")

        return request.render('survey.certification_share_view', values)
