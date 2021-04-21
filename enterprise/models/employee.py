from odoo import fields, api, models
import datetime
from odoo.tools.translate import _
from odoo.exceptions import UserError, ValidationError, Warning
from dateutil import relativedelta


class EnterpriseEmployee(models.Model):
    _name = 'enterprise.employee'
    _description = 'Employee of our enterprise'
    _inherit = 'enterprise.client'
    # _rec_name = 'f_name'

    date_start = fields.Date(string='Date of start')
    time_working = fields.Char(string='Time of working',
                               compute='_get_time_worked')
    salary = fields.Integer(string='Salary')
    salary_premium = fields.Integer(string='Premium Salary')
                                #compute='_get_salary')
    salary_total = fields.Integer(string='Salary total', compute='total_salary')
    department_id = fields.Many2one(string='Department',
                                    comodel_name='enterprise.department')
    job_uid = fields.Many2one(string='Job',
                              comodel_name='enterprise.job')
    client_uid = fields.One2many(string='clients',
                                 comodel_name='enterprise.client',
                                 inverse_name='employee_uid')
    # product_uid = fields.One2many(string='Products',
    #                               comodel_name='enterprise.product',
    #                               inverse_name='employee_uid')
    # order_id = fields.One2many(string='Order',
    #                            comodel_name='enterprise.product.order',
    #                            inverse_name='product_sold_by')

    @api.depends('salary', 'salary_premium')
    def total_salary(self):
        for rec in self:
            if rec.salary and rec.salary_premium:
                rec.salary_total = rec.salary + rec.salary_premium
            else:
                rec.salary_total = rec.salary

    def wiz_open_salary(self):
        print('wos : ', self.env['ir.actions.act_window']._for_xml_id('enterprise.employee_salary_premium_update_action'))

        return self.env['ir.actions.act_window']._for_xml_id('enterprise.employee_salary_premium_update_action')

    # used for wizard
    def wiz_open(self):
        # that return as you see bellow instead the second return
        print('wo : ', self.env['ir.actions.act_window']._for_xml_id('enterprise.employee_password_update_action'))
        return self.env['ir.actions.act_window']._for_xml_id('enterprise.employee_password_update_action')
        # return {'type': 'ir.actions.act_window',
        #         'res_model': 'employee.password.update.wiz',
        #         'view_mode': 'form',
        #         'target': 'new'
        #         }

    # function used to set value of salary to some employee greater or less then we have declared above
    # @api.model
    # def create(self, values):
    #     if values['job_uid'] == 2 and values['salary'] < 7000:
    #         raise ValidationError(f'Error the Doctor job cant have less then 7000 '
    #                               f'and you past just {values["salary"]} MAD')
    #     if values['job_uid'] == 1 and values['salary'] < 9500:
    #         raise ValidationError(f"Error Manager job cant be less then 9500 "
    #                               f"and you past {values['salary']} MAD")
    #     if values['job_uid'] == 3 and values['salary'] < 5000:
    #         raise ValidationError(f"Error of Nurse job cant be less then 5000 "
    #                               f"and you past {values['salary']} MAD")
    #     if values['job_uid'] == 4 and values['salary'] < 4000:
    #         raise ValidationError(f"Error the Maid job cant be less then 4000"
    #                               f" and you past {values['salary']}")
    #     if values['job_uid'] == 5 and (values['job_uid'] < 3500 or values['salary'] > 4500):
    #         raise ValidationError(f"Error the Driver job range of salary is between 3500 MAD and 4500 MAD "
    #                               f"and you past just {values['salary']} MAD")
    #     print(values['job_uid'])
    #     rtn = super(EnterpriseEmployee, self).create(values)
    #     return rtn

    # def write(self, values):
    #     # print(self)
    #     # print(values)
    #     # print(f'salary value before calculation {values["salary"]}')
    #     if values['salary'] > 5000:
    #         values['salary'] = values['salary'] - 1000
    #     # print(f'value of salary after calculation {values["salary"]}')
    #     rtn = super(EnterpriseEmployee, self).write(values)
    #     # print(rtn)
    #     return rtn

    # function used to get lot of data instead _rec_name where we can use just one data
    def name_get(self):
        list_rec_name = []
        for rec in self:
            rec_name = rec.l_name if rec.l_name else 'empty'
            if rec.f_name and rec.department_id.name and rec.job_uid.name:
                rec_name += f' {rec.f_name}, {rec.job_uid.name}, {rec.department_id.name}'
            list_rec_name.append((rec.id, rec_name))
        return list_rec_name

    # function used to calculate how much the employee worked from date of start
    # and she display data as " years - months - days "
    @api.onchange('date_start')
    def _get_time_worked(self):
        today = datetime.date.today()
        for rec in self:
            if rec.date_start:
                d_start = fields.Datetime.to_datetime(rec.date_start).date()
                total = relativedelta.relativedelta(today, d_start)
                x, y, z = 'year', 'month', 'day'
                if total.years > 1:
                    x = 'years'
                if total.months > 1:
                    y = 'months'
                if total.days > 1:
                    z = 'days'
                rec.time_working = f'{total.years} {x} / {total.months} {y} / {total.days} {z}'
            else:
                rec.time_working = 'Not Provided'

    @api.model
    def name_search(self, name, args=None, operator='ilike', limit=100):
        args = args or []
        if name:
            data = self.search(['|', '|', '|', ('f_name', operator, name), ('l_name', operator, name),
                                ('email', operator, name), ('phone', operator, name)])
            return data.name_get()
        return self.search([('f_name', operator, name)]+args, limit=limit).name_get()

    # @api.model
    # def create(self, values):
    #     print(self)
    #     print(values)
    #     print(values['salary'])
    #     # values['salary'] = values['salary'] + 100
    #     if values['salary'] > 5000:
    #         values['salary'] = values['salary'] - 1000
    #     email_list = ['@gmail.fr', '@gmail.com', '@hotmail.com',
    #                   '@hotmail.fr']
    #     print(values['email'])
    #     if values['email'].endswith('@hotmail.com'):
    #         print('yes')
    #     for i in email_list:
    #         # if i not in values['email']:
    #         print(i)
    #         s = values['email'].endswith(i)
    #         if True:
    #             print('yes also')
    #             # raise ValidationError(_('Error email invalid'))
    #
    #     rtn = super(EnterpriseEmployee, self).create(values)
    #     print(rtn)
    #     return rtn

    # @api.model
    # def create(self, values):
    #     print(f"self : {self}")
    #     print(f'values  :  {values}')
    #     print(values['salary'])
    #     # for rec in self:
    #     #     if rec.salary > 5000.00:
    #     #         s = rec.salary - 1000
    #     # values = values['salary'] + 200
    #     rtn = super(EnterpriseEmployee, self).create(values)
    #     print(rtn)
    #     return rtn



            # print('total appended to list', y)
            # print('y', y[0])
            # s = y[0]
            # print('y', type(y[0]))
            # print('d_start   :   ', d_start)
            # print('total   :  ', total)
            # print('total in month  :  ', total.months)
            # print('total in year :  ', total.years)
            # s = [str(total.years) + ' years', str(total.months) + ' months', str(total.days) + ' days']
            # print(s)

    # @api.model
    # def default_get(self, fields_list=[]):
    #     print(f' field_list :  {fields_list}')
    #     rtn = super(EnterpriseEmployee, self).default_get(fields_list)
    #     print(f'My_rtn before editing was empty:   {rtn}')
    #     rtn['l_name'] = 'Your last name'
    #     rtn['f_name'] = 'Your First name'
    #     rtn['email'] = 'abcd@gmail.com'
    #     rtn['password'] = '**********'
    #     # rtn['d_birth'] = '01-01-2021' unavailable this fields cant have default data Date
    #     rtn['gender'] = 'Male'
    #     rtn['phone'] = '+212 762804521'
    #     # rtn['job_uid'] = 'Job'   unavailable
    #     print(f'Know after my rtn was modified :   {rtn}')
    #     return rtn

    # @api.model
    # def create(self, values):
    #     print('self :  ', self)
    #     print('values :  ', values)
    #     for rec in values.keys():
    #         print(rec)
    #         if rec == 'False':
    #             rec = '----'
    #     rtn = super(EnterpriseEmployee, self).create(values)
    #     return rtn
