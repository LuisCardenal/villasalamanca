from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
import re


class ResPartner(models.Model):
    _inherit = 'res.partner'

    document_nit = fields.Char(string='NIT', size=17, required=True,
                               help='Ingrese número de NIT Ej: 0123-456789-123-1')
    document_giro = fields.Char(string='Giro')
    document_dui = fields.Char(string='DUI', size=10, help='Ingrese número de DUI Ej: 12345678-9')
    journal_contacts = fields.Many2one(comodel_name='account.journal', string='Diario contable enlazado')
    # vat = fields.Char(string='Identificación Fiscal / NRC')
    _sql_constraints = [
        ('nit_uniq', 'unique (document_nit)', 'El número ingresado ya existe en la base de datos')
    ]

    @api.onchange('email')
    def validate_mail(self):
        if self.email:
            match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', self.email)
            if match == None:
                raise ValidationError('Correo electrónico inválido. Intente nuevamente')

    @api.onchange('document_nit')
    def validate_nit(self):
        if self.document_nit:
            match = re.match('^\+?[0-9]{4}[-][0-9]{6}[-][0-9]{3}[-][0-9]{1}$', self.document_nit)
            if match == None:
                raise ValidationError(
                    'Número de NIT inválido. Intente nuevamente siguiendo el siguiente patrón:  0123-456789-123-1')

    @api.onchange('document_dui')
    def validate_dui(self):
        if self.document_dui:
            match = re.match('^\+?[0-9]{8}[-][0-9]{1}$', self.document_dui)
            if match == None:
                raise ValidationError(
                    'Número de DUI inválido. Intente nuevamente siguiendo el siguiente patrón:  12345678-9')
