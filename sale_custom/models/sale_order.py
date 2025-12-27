from odoo import models, fields
from odoo.exceptions import UserError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    is_priority = fields.Boolean(string="Priority Order")

    def action_confirm(self):


        for order in self:
            if order.is_priority and order.amount_total < 10000:
                raise UserError(
                    "A priority order can only be confirmed if its value exceeds 10,000."
                )

        result = super(SaleOrder, self).action_confirm()

        for order in self:
            if order.is_priority:
                order.message_post(
                    body="This request has been confirmed as a priority request."
                )

        return result
