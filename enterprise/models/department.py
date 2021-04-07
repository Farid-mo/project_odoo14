from odoo import fields, api, models


class EnterpriseDepartment(models.Model):
    _name = 'enterprise.department'
    _description = 'All department of our enterprise'

    name = fields.Char(string='Name')
    code_dep = fields.Char(string='Code of department')
    employee_uid = fields.One2many(string='Employee',
                                   comodel_name='enterprise.employee',
                                   inverse_name='department_id')

    @api.model
    def name_search(self, name, args=None, operator='ilike', limit=100):
        args = args or []
        if name:
            data = self.search(['|', ('name', operator, name), ('code_dep', operator, name)])
            return data.name_get()
        return self.search([('name', operator, name)] + args, limit=limit).name_get()
