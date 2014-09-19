# -*- coding: utf-8 -*-
#!/usr/bin/env python
{
	'name': 'Curso OpenERP',
	'descripcion' : 'Este módulo es para aprender OpenERP',
	'autor' : 'Luis Torres',
    'version' : 'dia1',
    'depends' : ['base', 'mail', ],
    'data' : [
        'security/curso_odoo_security.xml',
        'views/curso_odoo_view.xml',
        'views/multimedia_view.xml',
        'views/tipo_medio_view.xml',
        'views/suscriptor_view.xml',
        'views/tienda_view.xml',
        'views/suscripcion_view.xml',
        'views/categoria_view.xml',
        'views/solicitud_view.xml',
        'security/menu_security.xml',
        'data/suscripcion_data.xml',
        'security/ir.model.access.csv'

    ],
    'demo' : [],
    
}