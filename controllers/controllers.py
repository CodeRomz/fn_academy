# -*- coding: utf-8 -*-
# from odoo import http


# class FnAcademy(http.Controller):
#     @http.route('/fn_academy/fn_academy', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fn_academy/fn_academy/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('fn_academy.listing', {
#             'root': '/fn_academy/fn_academy',
#             'objects': http.request.env['fn_academy.fn_academy'].search([]),
#         })

#     @http.route('/fn_academy/fn_academy/objects/<model("fn_academy.fn_academy"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fn_academy.object', {
#             'object': obj
#         })

