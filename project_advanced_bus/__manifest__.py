# -*- coding: utf-8 -*-
{
    'name': "Real Time Project Task Management",

    'summary': """
        All tasks will update realtime
        """,

    'description': """
        Just install/upgrade do not need configuration
        All tasks will update realtime.
        When any project user change a task stage, all users are looking at same project will see new change.
    """,

    'author': "Magenest",
    'website': "https://store.magenest.com",
    'category': 'Project',
    'version': '1.0',
    'license': 'OPL-1',
    'depends': ['base', 'project', 'mail', 'bus', 'web'],
    'data': [
        'views/project_longpolling_template.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}