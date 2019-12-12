# © 2016-2017 Akretion (Alexis de Lattre <alexis.delattre@akretion.com>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Base Factur-X/ZUGFeRD',
    'version': '11.0.1.0.0',
    'category': 'Accounting & Finance',
    'license': 'AGPL-3',
    'summary': 'Base module for Factur-X and ZUGFeRD',
    'author': 'Akretion,Odoo Community Association (OCA)',
    'website': 'http://www.akretion.com',
    'depends': [
        'product_uom_unece',
        'account_tax_unece',
        'account_payment_unece',
        ],
    'data': ['data/zugferd_codes.xml'],
    'installable': True,
}
