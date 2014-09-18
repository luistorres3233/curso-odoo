# -*- coding: utf-8 -*-

from openerp.osv import osv, fields

TIPOS = [
    ('oro','Plan Oro'), 
    ('plata', 'Plan Plata'), 
    ('bronce', 'Plan Bronce'),
]

class suscripcion(osv.osv):
    _name = 'co.suscripcion'
    _descripcion = 'CO Suscripcion'

    _columns = {


        'codigo': fields.char('Código'),
        'tipo': fields.selection(TIPOS,'tipo de suscripción'),
        'fecha_inicio': fields.date('fecha inicio suscripción'),
        'fecha_final': fields.date('fecha final suscripción'),
        'activo': fields.boolean('activo'),
        'suscriptor_id': fields.many2one('co.suscriptor', 'afiliado'),
        
    }

suscripcion()
