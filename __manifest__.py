# -*- coding: utf-8 -*-
##############################################################################
#                 @author dcrsoluciones.com
#
##############################################################################

{
    'name': 'Vista detallada de facturas',
    'version': '16.01',
    'description': ''' Descripción detallada en la vista de las facturas
    ''',
    'category': 'Accounting',
    'author': 'DCR Soluciones',
    'website': 'dcrsoluciones.com',
    'depends': [
        'base', 'account',
    ],
    'data': [
        'views/account_invoice_view.xml',
        'views/custom_invoice_report.xml',
    ],
    'application': False,
    'installable': True,
    'price': 0.00,
    'currency': 'USD',
    'license': 'OPL-1',	
}
