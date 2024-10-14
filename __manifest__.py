# -*- coding: utf-8 -*-
{
    'name': "Firenor Academy",

    'summary': "Firenor Academy eLearning",

    'description': """
                    Firenor Academy eLearning
    """,

    'author': "Romualdo Jr ",
    'website': "https://github.com/CodeRomz/fn_academy.git",

    'category': 'Website/eLearning',
    'version': '17.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['survey'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/views.xml',
        # 'report/report.xml',
    ],
    'installable': True,
    'application': True,

    'web.report_assets_common': [
        'fn_academy/static/src/scss/survey_reports_custom.scss',
    ],

}
