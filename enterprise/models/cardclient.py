from odoo import fields, api, models


class EnterpriseProductOrder(models.Model):
    _name = 'enterprise.product.order'
    _description = 'each order has employee responsible and client'
    # _inherit = 'enterprise.'

    # product_belong = fields.Many2many(string='Sold by', comodel_name='enterprise.product')
    # product_needed_by = fields.Many2many(string='bought by', comodel_name='enterprise.client')
    # content = fields.Text(string='context')
    # quantity_info = fields.Integer(string='Quantity available')
    product_sold_by = fields.Many2one(string='Sold by', comodel_name='enterprise.employee')
    # product_id = fields.Many2many(string='Product', comodel_name='enterprise.product')
    # product_needed_by = fields.Many2one('enterprise.client', 'bought by')

    # @api.onchange('product_needed_by')
    # def _onchange_product_needed_by(self):
    #     print(self.product_needed_by)
    #     for rec in self.product_needed_by.f_name:
    #         # if rec.product_needed_by:
    #         #     rec.product_needed_by = rec.product_needed_by.f_name + ' ' + rec.product_needed_by.l_name
    #         print(rec)

        # self.product_needed_by += self.product_needed_by.l_name



    # @api.model
    # def create(self, values):
    #     print(self)
    #     print(values)
    #     rtn = super(EnterpriseProductOrder, self).create(values)
    #     return rtn
    # @api.onchange('product_needed_by')
    # def concatenate(self):
    #     self.product_needed_by = self.env['enterprise.client'].f_name

    #
    # @api.depends('quantity')
    # def check_quantity(self):
    #     rtn = self.env['enterprise.product'].search([('quantity', 'like', self.quantity)])
    #     if rtn:
    #         print(rtn)
    #     print(rtn)
    #     return rtn
    #
    # @api.depends('product_id')
    # def _get_value_quantity(self):
    #     print(self)
    #     # print(self.quatity)
    #     for rec in self:
    #         if rec.product_id:
    #             print(rec.product_id)
    #             print('yes')
    #         else:
    #             print('no')