from odoo import fields, models


class EmployeeCreate(models.TransientModel):
    _name = "create.client.card.wizard"
    _description = 'Wizard used to create card for client'

    l_name = fields.Char(string='Last name')
    number_account = fields.Char(string='Card Number')
    expiration_date = fields.Date(string='Expiration Date')
    cvv = fields.Integer(string='CVV')
    client_ids = fields.Many2one(string='Client responsible', comodel_name='enterprise.client')

    def create_client_card_wizard(self):
        return self.env['enterprise.client.card'].browse(self._context.get('active_ids')).create({'l_name': self.l_name,
                                                                                                  'number_account': self.number_account,
                                                                                                  'expiration_date': self.expiration_date,
                                                                                                  'cvv': self.cvv,
                                                                                                  'client_ids': self.client_ids.id})


