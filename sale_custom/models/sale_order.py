from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    is_priority = fields.Boolean(string="Priority Order")
