# -*- coding: utf-8 -*-

from openerp.osv import osv, fields

    
class categoria(osv.osv):
    _name = 'co.categoria'
    _descripcion = 'CO categoria'

    _columns = {

        'nombre': fields.char('nombre de la categoria'),
        'descripcion': fields.text('descripción'),
        'parent_id': fields.many2one('co.categoria', 'Padre'),
        'child_ids': fields.one2many(
            'co.categoria', 
            'parent_id', 
            'Sub-categoria'),
        
    }        

categoria()
