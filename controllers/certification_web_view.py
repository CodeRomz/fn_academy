from odoo import http
from odoo.http import request

class SurveyCertificateController(http.Controller):
    @http.route(['/fna/certification/<int:user_input_id>'], type='http', auth='public', website=True)
    def view_certificate(self, user_input_id, **kwargs):
        # Fetch the survey response using sudo() to bypass security restrictions
        user_input = request.env['survey.user_input'].sudo().browse(user_input_id)
        if not user_input.exists():
            return request.not_found()

        # Prepare values for rendering
        values = {
            'docs': user_input,
            'share_url': request.httprequest.host_url + 'fna/certification/' + str(user_input_id)
        }
        return http.request.render('survey.certification_report_view', values)
