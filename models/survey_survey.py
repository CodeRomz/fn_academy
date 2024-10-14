from odoo import models, fields

class Survey(models.Model):
    _inherit = 'survey.survey'

    # Override the field with a new method to remove existing selections
    certification_report_layout = fields.Selection(
        selection=lambda self: [('firenorV1_seagreen', 'Firenor V1 Seagreen')],
        string='Certification Template',
        default='firenor_seagreen'
    )
