# -*- coding: utf-8 -*-
{
    'name': "Firenor Academy",

    'summary': "Firenor Academy eLearning",

    'description': """
                    Firenor Academy eLearning
    """,

    'author': "Romualdo Jr ",
    'website': "https://github.com/CodeRomz/fn_academy.git",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Website/eLearning',
    'version': '17.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['survey'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/views.xml',
        # 'views/templates.xml',
    ],
}
