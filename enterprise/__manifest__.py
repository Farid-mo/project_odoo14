# -*- coding: utf-8 -*-
{
    'name': "Enterprise building",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",
    'category': 'Website',
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    # 'category': 'Uncategorized',
    'version': '1.0',
    'sequence': -100,
    # any module necessary for this one to work correctly
    'depends': [],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/main.xml',
        'reports/client_info.xml',
        'reports/report.xml',
        # 'security/ir.model.access.csv',
        'data/enterprise.job.csv',
        'data/enterprise.department.csv',
        # 'data/enterprise.product.csv',
        # 'data/enterprise.employee.csv',
        'wizard/employee_password_update_wizard_view.xml',
        'wizard/employee_salary_premium_wizard_view.xml',
        'wizard/employee_create_profile_wizard.xml',
        'wizard/client_create_card_wizard.xml',
        'views/job.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/client.xml',
        'views/employee.xml',
        'views/department.xml',
        'views/product.xml',
        'views/cardclient.xml',
        # 'reports/report.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
