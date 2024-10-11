# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class fn_academy(models.Model):
#     _name = 'fn_academy.fn_academy'
#     _description = 'fn_academy.fn_academy'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

