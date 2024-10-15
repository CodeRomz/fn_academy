from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class ResUsers(models.Model):
    _inherit = 'res.users'

    @api.model
    def action_redirect_to_slides(self):
        try:
            return {
                'type': 'ir.actions.act_url',
                'url': '/slides',
                'target': 'self',
            }
        except Exception as e:
            _logger.error(f"Error while redirecting to slides: {e}")
            raise
        else:
            _logger.info("Redirect action triggered successfully.")
        finally:
            _logger.info("Redirect to slides method executed.")
