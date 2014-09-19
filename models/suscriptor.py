# -*- coding: utf-8 -*-

from openerp.osv import osv, fields

class suscriptor(osv.osv):
    _name = 'co.suscriptor'
    _description = 'CO Suscriptor'
    _rec_name='nombre'
    
    _columns = {
        'nombre': fields.char('Nombre y Apellido'),
        'identificacion': fields.char('Cédula'),
        'direccion': fields.text('Dirección'),
            }

    _sql_constraints= [
    	('identificacion_unique', 'unique(identificacion)',u'Este número de cédula ya está registrado.'),

    ]

suscriptor()


        