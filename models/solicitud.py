# -*- coding: utf-8 -*-

from openerp.osv import osv, fields


class solicitud(osv.osv):
    _name = 'co.solicitud'
    _descripcion = 'CO solicitud'

    _columns = {

        'suscriptor_id': fields.many2one('co.suscriptor', 'afiliado'),
        'multimedia_id': fields.many2one('co.multimedia', 'multimedia'),
        'medio_id': fields.many2one('co.tipo.medio', 'tipo de medio'),
        'fecha solicitud': fields.date('fecha solicitada'),
        'cant_dias': fields.integer('duracion (en dias)'),
        

    }        

solicitud()
