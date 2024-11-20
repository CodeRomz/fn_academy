from odoo import http
from odoo.http import request, content_disposition

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
        return request.render('survey.certification_report_view', values)

    @http.route(['/fna/certification/<int:user_input_id>/image'], type='http', auth='public')
    def certificate_image(self, user_input_id, **kwargs):
        # Fetch the survey response
        user_input = request.env['survey.user_input'].sudo().browse(user_input_id)
        if not user_input.exists() or not user_input.certificate_image:
            return request.not_found()

        # Serve the certificate_image as a binary file
        image = user_input.certificate_image
        return request.make_response(
            image,
            headers=[
                ('Content-Type', 'image/png'),
                ('Content-Disposition', content_disposition('certificate_image.png')),
            ]
        )
