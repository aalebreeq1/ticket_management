# -*- coding: utf-8 -*-
{
    'name': 'Ticket Management System',
    'version': '19.0.1.0.0',
    'summary': 'Module for managing helpdesk and support tickets',
    'author': 'Abdulla Alebreeq',
    'category': 'Services/Helpdesk',
    'license': 'AGPL-3',
    'depends': [
        'base',
        'mail',
    ],
    'data': [
        'security/ticket_security.xml',
        'security/ir.model.access.csv',
        'security/ticket_record_rules.xml',
        'data/ticket_sequence.xml',
        'views/ticket_supporting_view.xml',
        'views/ticket_views.xml',
        'views/menu_views.xml',
        'data/ticket_demo.xml',
        
    ],

    'installable': True,
    'application': True,
    'auto_install': False,
}