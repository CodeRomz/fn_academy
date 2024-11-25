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
    'depends': ['website', 'survey'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/fn_acad_security_rules.xml',
        'views/res_users.xml',
        'views/survey_user_views.xml',
        'report/custom_survey_template.xml',
        'report/custom_survey_reports.xml',

    ],
    'installable': True,
    'application': True,
}
