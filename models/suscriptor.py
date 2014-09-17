# -*- coding: utf-8 -*-

from openerp.osv import osv, fields

class suscriptor(osv.osv):
    _name = 'co.suscriptor'
    _description = 'CO Suscriptor'
    
    _columnas = {
        'nombre': fields.char('Nombre y Apellido'),
        'identificacion': fields.char('Cédula'),
        'direccion': fields.text('Dirección'),
    }

suscriptor()


        