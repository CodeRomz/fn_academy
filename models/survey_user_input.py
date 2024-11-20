from odoo import models, fields

class SurveyUserInput(models.Model):
    _inherit = 'survey.user_input'

    certificate_image = fields.Image("Certificate Image")
