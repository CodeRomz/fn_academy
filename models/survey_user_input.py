from odoo import models, fields, api, tools, _
from odoo.exceptions import (
    UserError,
    ValidationError,
    RedirectWarning,
    AccessDenied,
    AccessError,
    CacheMiss,
    MissingError,
)
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

    # Non-stored computed field for public access
    certificate_image_public = fields.Image(
        "Certificate Image (Public)",
        compute='_compute_certificate_image_public',
        store=False  # Fetches dynamically; no duplication in the database
    )

    @api.depends('certificate_image')
    def _compute_certificate_image_public(self):
        """
        Dynamically compute the public version of the certificate image.
        This allows the image to bypass access rights for public users.
        """
        for record in self:
            try:
                record.certificate_image_public = record.sudo().certificate_image
            except Exception as e:
                _logger.error(f"Error computing public certificate image: {e}")
                record.certificate_image_public = False
