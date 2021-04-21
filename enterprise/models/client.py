from odoo import fields, api, models
import datetime
# from odoo.tools.translate import _
# from odoo.exceptions import UserError, ValidationError, Warning


class EnterpriseClient(models.Model):
    _name = 'enterprise.client'
    _description = "Clients of our Enterprise"
    # _inherit = 'enterprise.product.order'
    # _rec_name = 'f_name'

    email = fields.Char(string="Email")
    password = fields.Char(string='Password')
    f_name = fields.Char(string='First name')
    l_name = fields.Char(string='Last name')
    d_birth = fields.Date(string='Date of birth')
    age = fields.Char(string='Your age', compute='_get_age')
    gender = fields.Selection([('Male', 'Male'), ('Female', 'Female'),
                               ('Other', 'Other')])
    phone = fields.Char(string='Number Phone')
    employee_uid = fields.Many2one(string='employees responsible',
                                   comodel_name='enterprise.employee')
    card_ids = fields.One2many(string='Cards', comodel_name='enterprise.client.card',
                               inverse_name='client_ids')

    def name_get(self):
        list_rec_name = []
        for rec in self:
            rec_name = rec.f_name if rec.f_name else 'empty'
            # print(f' rec_name before edited ::  {rec_name}')
            if rec.l_name:
                rec_name += f' {rec.l_name}'
                # print(f"rec name after add l_name ::  {rec_name}")
            list_rec_name.append((rec.id, rec_name))
            # print(f" list_rec_name  ::  {list_rec_name}")
        return list_rec_name

    @api.onchange('d_birth')
    def _get_age(self):
        today = datetime.date.today()
        for ages in self:
            if ages.d_birth:
                d_birth = fields.Datetime.to_datetime(ages.d_birth).date()
                total = str(int((today - d_birth).days / 365))
                ages.age = total
            else:
                ages.age = 'Not Provided'

    # @api.model
    # def _name_search(self, name='', args=None, operator=' i like', limit=100, name_get_uid=None):
    #     args = args or []
    #     domain = []
    #     if name:
    #         domain = ['|', '|', ('f_name', operator, name), ('l_name', operator, name), ('email', operator, name)]
    #     values = self.search(domain+args, limit=limit)
    #     return values.name_get()
