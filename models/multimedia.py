# -*- coding: utf-8 -*-

from openerp.osv import osv, fields


class multimedia(osv.osv):
    _name = 'co.multimedia'
    _descripcion = 'CO multimedia'

    _columns = {

        'titulo': fields.char('Título', required=True),
        'codigo': fields.char('Código'),
        'fecha_publicacion': fields.date('Fecha de Publicación'),
        'categoria_id': fields.many2one('co.categoria', 'Categoría'),
        'medio_ids': fields.many2many('co.tipo.medio', 'co_multimedia_medio_rel', 'multimedia_id', 'medio_id'),


    }




multimedia()
