from odoo import models, fields, api


class AccountJournal(models.Model):
    _inherit = 'account.journal'

    num_correlativo = fields.Char(string='Número de correlativo: ', readonly=True, default=1)


