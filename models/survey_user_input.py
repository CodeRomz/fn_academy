from odoo import models, fields


class SurveyUserInput(models.Model):
    _inherit = 'survey.user_input'

    cert_name = fields.Char(string='Certification', compute="_compute_cert_name")


    def _compute_cert_name(self):
        for records in self:
            records.cert_name = str(records.survey_id.display_name) + " - " + str(records.partner_id.display_name) + " - " + str(records.create_date)