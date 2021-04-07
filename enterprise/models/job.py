from odoo import fields, api, models


class EmployeeJob(models.Model):
    _name = 'enterprise.job'
    _description = 'Employee jobs'
    _inherit = 'enterprise.client'

    name = fields.Char(string='Jobs')
    content = fields.Char(string='check')
    salary = fields.Char(string='salary')
    employee_uid = fields.One2many(string='employee job',
                                   comodel_name='enterprise.employee',
                                   inverse_name='job_uid')

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
    #     if not values['email'].endswith('@gmail.fr' or '@gmail.com' or
    #                                     '@hotmail.com' or '@hotmail.fr'):
    #         raise ValueError('Error invalid email')
    #
        #     print('yes')
        # for i in email_list:
        #     # if i not in values['email']:
        #     print(i)
        #     s = values['email'].endswith(i)
        #     if True:
        #         print('yes also')
                # raise ValidationError(_('Error email invalid'))
        #
        # rtn = super(EmployeeJob, self).create(values)
        # print(rtn)
        # return rtn


    # def name_get(self):
    #     list_name = []
    #     for rec in self:
    #         name = rec.name if rec.name else 'empty'
    #         # print(f' name :  {name}')
    #         if rec.content:
    #             name += f' - {rec.content}'
    #         list_name.append((rec.id, name))
    #         # print(f' list_name :  {list_name}')
    #     return list_name

