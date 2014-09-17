# -*- coding: utf-8 -*-

from openerp.osv import osv, fields


class linea_stock(osv.osv):
    _name = 'co.linea.stock'
    _descripcion = 'CO linea_stock'

    _columns = {

        'multimedia_id': fields.many2one('co.multimedia', 'Multimedia'),
        'medio_id': fields.many2one('co.tipo.medio', 'tipo medio'),
        'tienda_id': fields.many2one('co.tienda', 'tienda'),
        'quantity': fields.integer('cantidad')
        

    }        

linea_stock()

class tienda(osv.osv):
	_inherit = 'co.tienda'

	_columns = {

	'linea_stock': fields.one2many('co.linea_stock', 'stock')

	}

tienda()