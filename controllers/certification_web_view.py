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
        # Fetch the survey response using sudo() to bypass security restrictions
        user_input = request.env['survey.user_input'].sudo().browse(user_input_id)
        if not user_input.exists():
            _logger.warning(f"User input with ID {user_input_id} not found.")
            return request.not_found()

        # Prepare values for rendering
        values = {
            'docs': user_input,
            'share_url': f"{request.httprequest.host_url}fna/certification/{user_input_id}",
        }
        return request.render('survey.certification_report_view', values)

    @http.route('/fna/certification/web/<int:user_input_id>/', auth='public', website=True)
    def view_web_certificate(self, user_input_id, **kwargs):
        """
        Render the certification page for the given user_input_id.
        """

        # Log the attempt to fetch the user input
        _logger.info(f"Attempting to fetch user input with ID: {user_input_id}")

        # Manually fetch the survey response without automatic slug behavior
        user_input = request.env['survey.user_input'].sudo().browse(user_input_id)

        # Ensure the record exists
        if not user_input.exists():
            _logger.warning(f"User input with ID {user_input_id} not found.")
            return request.not_found()

        # Prepare rendering values
        values = {
            'user_input': user_input,
        }

        # Log the rendering action
        _logger.info(f"Rendering certification for user input ID {user_input_id}")

        # Render the certification page using the custom view
        return request.render('survey.certification_web_view', values)