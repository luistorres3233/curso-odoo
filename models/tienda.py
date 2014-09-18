# -*- coding: utf-8 -*-

from openerp.osv import osv, fields


class tienda(osv.osv):
    _name = 'co.tienda'
    _descripcion = 'CO tienda'
    _rec_name = 'nombre'

    _columns = {

        'nombre': fields.char('nombre tienda', required=True),
        'direccion': fields.char('ubicación física de la tienda'),
        

    }        

tienda()
