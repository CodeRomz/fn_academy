from odoo import _, api, fields, models

class SurveySurvey(models.Model):
    _inherit = 'survey.survey'

    # Extend the certification_report_layout selection field to add 'firenor_v1'
    certification_report_layout = fields.Selection(
        selection_add=[
            ('firenor_v1', 'Firenor V1')
        ],
    )
