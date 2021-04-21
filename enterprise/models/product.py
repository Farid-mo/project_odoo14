from odoo import fields, api, models
from odoo.exceptions import ValidationError


class EnterpriseProducts(models.Model):
    _name = 'enterprise.product'
    _description = "Many of those product belong to each employee"
    # _inherit = ['enterprise.client',]

    price = fields.Integer(string='Price of Product')
    # quantity = fields.Integer(string='Quantity')
    # price_total = fields.Integer(string='Price total to pay', compute='_get_price_unite')
    # employee_uid = fields.Many2one('enterprise.employee', string='Product responsible')
    # order_id = fields.Many2many(string='Orders',
    #                             comodel_name='enterprise.product.order')

    # @api.onchange('price', 'quantity')
    # def _get_price_unite(self):
    #     for rec in self:
    #         if rec.price:
    #             rec.price_total = rec.quantity * rec.price
    #         else:
    #             rec.price_total = rec.price
