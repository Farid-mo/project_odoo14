from odoo import fields, api, models


class EmployeeCreate(models.TransientModel):
    _name = "employee.create.record.wizard"
    _description = 'Wizard used to create new record in table employee'

    f_name = fields.Char(string='First name')
    l_name = fields.Char(string='Last name')
    phone = fields.Char(string='Number Phone')
    email = fields.Char(string="Email")
    password = fields.Char(string='Password')
    date_start = fields.Date(string='Date of start')
    job_uid = fields.Many2one(string='Job    (M2O.F)',
                              comodel_name='enterprise.job')
    department_id = fields.Many2one(string='Department   (M2O.F)',
                                    comodel_name='enterprise.department')
    client_uid = fields.One2many(string='clients    (O2M.F)',
                                 comodel_name='enterprise.client',
                                 inverse_name='employee_uid')

    # Create employee ( f-l_name, phone, email, password )
    def create_employee_wizard(self):
        return self.env['enterprise.employee'].browse(self._context.get('active_ids')).create({'f_name': self.f_name,
                                                                                               'l_name': self.l_name,
                                                                                               'phone': self.phone,
                                                                                               'date_start': self.date_start,
                                                                                               'job_uid': self.job_uid.id,
                                                                                               'department_id': self.department_id.id,
                                                                                               'client_uid': self.client_uid.id,
                                                                                               'email': self.email,
                                                                                               'password': self.password})
