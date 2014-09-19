# -*- coding: utf-8 -*-

from openerp.osv import osv, fields


class linea_stock(osv.osv):
    _name = 'co.linea.stock'
    _description = 'CO linea_stock'

    _columns = {

        'multimedia_id': fields.many2one('co.multimedia', 'Multimedia', required=True),
        'medio_id': fields.many2one('co.tipo.medio', 'tipo medio', required=True),
        'tienda_id': fields.many2one('co.tienda', 'tienda'),
        'cantidad': fields.integer('cantidad', required=True),
        

    }        

    def onchange_medio_id(self, cr, uid, ids, medio_id):
        return {

            'value': {
                'multimedia_id': False,
                'cantidad':0,

            }

        }

    def _check_qty(self, cr, uid, ids, context=None):
        if isinstance(ids, (int, long)):
            ids = [ids]
        for s in self.browse(cr, uid, ids, context=context):
            if s.cantidad < 0:
                return False
        return True

    _constraints = [
        (_check_qty, 'La cantidad no puede ser negativa', ['cantidad'])

    ]

    _sql_constraints= [
        ('stock_media_tienda', 'unique(medio_id, tienda_id, multimedia_id)', u'Ya está definido el stock, actualice.')

    ]


linea_stock()

class tienda(osv.osv):
    _inherit = 'co.tienda'

    _columns = {

	'linea_stock': fields.one2many('co.linea.stock','tienda_id', 'Stock')

	}

    def unlink(self, cr, uid, ids, context=None):
        if isinstance(ids,(int,long)):
            ids = [ids]

        for t in self.browse(cr, uid, ids, context=context):
            linea_stock = [l.id for l in t.linea_stock]
            if self.pool.get('co.linea.stock').unlink(cr, uid, linea_stock):
                if super(tienda, self).unlink(cr, uid, t.id, context=context):
                    continue
                return False
        return True

tienda()
