# -*- coding: utf-8 -*-
{
    'name': 'Ticket Management System',
    'version': '19.0.1.0.0',
    'summary': 'Module for managing helpdesk and support tickets',
    'author': 'Abdulla Alebreeq',
    'category': 'Services/Helpdesk',
    'license': 'AGPL-3',
    'depends': [
        'oi_workflow'
    ],
    'data': [
        'security/ticket_security.xml',
        'security/ir.model.access.csv',
        'security/ticket_record_rules.xml',
        'data/ticket_sequence.xml',
        'data/approval_config.xml',
        'data/approval_buttons.xml',
        'views/ticket_views.xml',
        'views/category_views.xml',
        'views/tag_views.xml',
        'views/menu_views.xml',
    ],

    'installable': True,
    'application': True,
    'auto_install': False,
}