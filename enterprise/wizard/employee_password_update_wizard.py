from odoo import fields, api, models


class EmployeePasswordUpdate(models.TransientModel):
    _name = "employee.password.update.wiz"
    _description = 'Wizard used to make simple pop-up where he can modify password'

    password = fields.Char(string='Password')

    def update_employee_password(self):
        # print('Successfully updated')
        self.env['enterprise.employee'].browse(self._context.get('active_ids')).update({'password': self.password})
        # return True
