from odoo import fields, api, models


class EmployeeSalaryPremium(models.TransientModel):
    _name = 'employee.salary.premium'
    _description = 'Wizard used to help user with pop-up to add multiple salary premium'

    salary = fields.Integer(string='Salary Plus premium')

    def update_employee_salary_premium(self):
        # None print('esp : ', self.env['enterprise.employee'].browse(self._context.get('active_ids')).update({'salary': self.salary}))
        print(self.salary)

        return self.env['enterprise.employee'].browse(self._context.get('active_ids')).write({'salary_premium': self.salary})

