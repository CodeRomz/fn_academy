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
        Fetch the certification page data for the given user_input_id.
        Log details to verify if fetching is successful.
        """

        # Log the attempt to fetch the user input
        _logger.info(f"Attempting to fetch user input with ID: {user_input_id}")

        # Manually fetch the survey response without automatic slug behavior
        user_input = request.env['survey.user_input'].sudo().browse(user_input_id)

        # Check if the record exists
        if not user_input.exists():
            _logger.warning(f"User input with ID {user_input_id} not found.")
            return request.not_found()

        # Log the successful fetching of the user input
        _logger.info(f"Successfully fetched user input: {user_input}")

        # Just return a simple response for now, confirming success
        return f"Successfully fetched user input with ID: {user_input_id}"