# -*- coding: utf-8 -*-

from openerp.osv import osv, fields
from datetime import datetime

TIPOS = [
    ('oro','Plan Oro'), 
    ('plata', 'Plan Plata'), 
    ('bronce', 'Plan Bronce'),
]

class suscripcion(osv.osv):
    _name = 'co.suscripcion'
    _descripcion = 'CO Suscripcion'
    _rec_name = 'codigo'

    _columns = {


        'codigo': fields.char('Código de Suscripción'),
        'tipo': fields.selection(TIPOS,'Tipo de Suscripción'),
        'fecha_inicio': fields.date('Fecha Inicio Suscripción'),
        'fecha_final': fields.date('Fecha Final Suscripción'),
        'activo': fields.boolean('Activo'),
        'suscriptor_id': fields.many2one('co.suscriptor', 'Afiliado'),
        
    }

    _defaults = {
    'activo': True,
    'fecha_inicio': datetime.now().strftime('%Y-%m-%d'),
    'codigo': lambda self, cr, uid, context: self.pool.get('ir.sequence').get(cr, uid, 'seq.suscripcion'),
    
    }

    def create(self, cr, uid, values, context=None):
        if context is None:
            context = {}
        values.update({'codigo': self.pool.get('ir.sequence').get(cr, uid, 'seq.suscripcion')})
        return super(suscripcion, self).create(cr, uid, values, context =context)

    

suscripcion()
