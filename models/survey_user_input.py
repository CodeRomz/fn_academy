from odoo import models, fields, api, _
import logging

_logger = logging.getLogger(__name__)

class SurveyUserInput(models.Model):
    _inherit = 'survey.user_input'

    # Storable field for uploading the certificate image
    certificate_image = fields.Image(
        "Certificate Image",
        max_width=1920,
        max_height=1080,  # Define maximum dimensions for storage
    )
