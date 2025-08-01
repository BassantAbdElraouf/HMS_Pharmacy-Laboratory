from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    type = fields.Selection(
        selection_add=[('medicine', 'Medicine')],
        ondelete={'medicine': 'set default'}
    )
