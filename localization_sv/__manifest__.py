# -*- coding: utf-8 -*-
{
    'name': "Localization SV",

    'summary': """
       """,

    'description': """
    Modulo para automatizar contabilidad de El Salvador.
    """,

    'author': "Rocketers",
    'website': "https://rocketters.com/",

    'category': 'Account',
    'version': '1',
    'license': 'LGPL-3',
    'summary': 'En este modulo se puede automatizar el apartado de reportes y facturas agregando nuevos campos relevantes.',

    # any module necessary for this one to work correctly
    'depends': ['account', 'base', 'contacts', 'hr', 'sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'security/account.account.csv',
        'data/account.account.template.csv',
        'report/asiento_contable_reporte.xml',
        'report/asiento_contable_reporte_view.xml',
        'report/report.xml',
        'report/factura_consumidor_final_exento_view.xml',
        'report/factura_credito_fiscal_view.xml',
        'report/report_consumidor_final_view.xml',
        'report/report_exportacion_view.xml',
        'report/report_nota_de_credito_view.xml',
        'report/report_nota_devolucion_view.xml',
        'views/hr_employee_view.xml',
        'views/res_partner_sv.xml',
        'report/sale_order_coti.xml',
        'report/report_credito_fiscal_exento_view.xml',
        'views/account_move_view_sv.xml',
        'views/account_journal_view.xml',

    ],
    # only loaded in demonstration mode
}
