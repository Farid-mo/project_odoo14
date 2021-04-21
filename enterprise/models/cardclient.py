from odoo import fields, api, models


class EnterpriseClientsCard(models.Model):
    _name = 'enterprise.client.card'
    _description = 'Client cards'
    # _inherit = 'enterprise.client'
    #
    l_name = fields.Char(string='Last Name')
    number_account = fields.Char(string='Card Number')
    expiration_date = fields.Date(string='Expiration Date')
    cvv = fields.Integer(string='CVV')
    client_ids = fields.Many2one(string='Client responsible', comodel_name='enterprise.client')
