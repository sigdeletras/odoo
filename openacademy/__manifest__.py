# -*- coding: utf-8 -*-
{
    'name': "Open Academy",

    'summary': """
        Ejemplo de módulo para gestión de curssos, asistentes""",

    'description': """
        Módulo de prueba
    """,

    'author': "Patricio Soriano",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/views.xml',
        'views/templates.xml',
        'views/openacademy.xml',
        'views/partner.xml',
        'reports/report_session.xml',
        'reports/report_course.xml',

    ],
    # Solo necesario para cargar datos de ejemplos
    'demo': [
        # 'demo/demo.xml',
    ],
}