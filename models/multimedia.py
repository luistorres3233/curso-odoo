# -*- coding: utf-8 -*-

from openerp.osv import osv, fields


class multimedia(osv.osv):
    _name = 'co.multimedia'
    _descripcion = 'CO multimedia'

    _columns = {

        'titulo': fields.char('título'),
        'codigo': fields.char('Código'),
        'fecha_publicacion': fields.date('fecha publicación'),
        'tipo_medio': fields.selection('fecha final suscripción'),
        'categoria_id': fields.many2one('co.categoria', 'categoría'),
        'medio_ids': fields.many2many('co.tipo.medio', 'co_multimedia_medio_rel', 'multimedia_id', 'medio_id'),


    }        

multimedia()
