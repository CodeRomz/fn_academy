from odoo import http
from odoo.http import request

# class SurveyCertificateController(http.Controller):
#     @http.route(['/fna/certification/<string:public_access_token>'], type='http', auth='public', website=True)
#     def view_certificate(self, public_access_token, **kwargs):
#         # Find the user input with the matching public access token
#         user_input = request.env['survey.user_input'].sudo().search([('public_access_token', '=', public_access_token)], limit=1)
#         if not user_input:
#             return request.not_found()
#
#         values = {
#             'doc': user_input,
#             'share_url': request.httprequest.host_url + 'fna/certification/' + public_access_token
#         }
#         return request.render('survey.certification_report_view', values)


class SurveyCertificateController(http.Controller):
    @http.route(['/fna/certification/<string:access_token>'], type='http', auth='public', website=True)
    def view_certificate(self, access_token, **kwargs):
        # Find the user input with the matching access token
        user_input = request.env['survey.user_input'].sudo().search([('access_token', '=', access_token)], limit=1)
        if not user_input:
            return request.not_found()

        values = {
            'docs': [user_input],  # Pass as list for compatibility with template looping
            'share_url': request.httprequest.host_url + 'fna/certification/' + access_token
        }
        return request.render('survey.certification_report_view', values)
