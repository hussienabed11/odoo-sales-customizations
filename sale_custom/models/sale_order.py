from odoo import models, fields, api
from odoo.exceptions import UserError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    is_priority = fields.Boolean(string="Priority Order")
    discount_amount = fields.Float(string="Priority Discount", compute="_compute_discount")

    @api.depends('is_priority', 'amount_total')
    def _compute_discount(self):
        for order in self:
            if order.is_priority:
                order.discount_amount = order.amount_total * 0.05
            else:
                order.discount_amount = 0.0
    @api.onchange('is_priority')
    def _onchange_is_priority(self):
        if self.is_priority:
            return {
                'warning': {
                    'title': "Priority Order",
                    'message': "This order is marked as priority! Discount will be applied automatically."
                }
            }

    def action_mark_as_priority(self):
        for order in self:
            if order.state not in ['draft', 'sent']:
                raise UserError(
                    "You can only mark draft or sent orders as priority."
                )

            order.is_priority = True
            order.message_post(
                body="This sale order has been marked as PRIORITY."
            )

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
