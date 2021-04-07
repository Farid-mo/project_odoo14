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
    'depends': ['base'],

    # always loaded
    'data': [
        'views/main.xml',
        # 'security/ir.model.access.csv',
        'data/enterprise.job.csv',
        'data/enterprise.department.csv',
        'views/job.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/client.xml',
        'views/employee.xml',
        'views/department.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
