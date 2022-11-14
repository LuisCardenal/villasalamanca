from odoo import models, fields, api


class AccountMove(models.Model):
    _inherit = 'account.move'

    journal_invoice = fields.Many2one(related='partner_id.journal_contacts', string='Diario relacionado: ', readonly=True)
    journal_id = fields.Many2one(string="Moneda en: ")


