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

    @http.route(['/fna/certification/<int:user_input_id>/image'], type='http', auth='public')
    def certificate_image(self, user_input_id, **kwargs):
        user_input = request.env['survey.user_input'].sudo().browse(user_input_id)
        if not user_input.exists():
            _logger.warning(f"User input with ID {user_input_id} not found.")
            return request.not_found()
        if not user_input.certificate_image:
            _logger.warning(f"No certificate image found for user_input_id: {user_input_id}")
            return request.not_found()

        mime_type = 'image/png'  # Default to PNG
        return request.make_response(
            user_input.certificate_image,
            headers=[
                ('Content-Type', mime_type),
                ('Content-Disposition', f'inline; filename=certificate_{user_input_id}.png'),
            ]
        )

