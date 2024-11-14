from odoo import http
from odoo.http import request

class SurveyCertificateController(http.Controller):
    @http.route(['/survey/certification/<int:user_input_id>'], type='http', auth='public', website=True)
    def view_certificate(self, user_input_id, **kwargs):
        user_input = request.env['survey.user_input'].sudo().browse(user_input_id)
        if not user_input.exists():
            return request.not_found()

        values = {
            'doc': user_input
        }
        # Update this line to ensure correct reference to the view
        return request.render('survey.certification_report_view', values)
