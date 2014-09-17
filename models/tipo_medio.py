# -*- coding: utf-8 -*-

from openerp.osv import osv, fields


class tipo.medio(osv.osv):
    _name = 'co.tipo.medio'
    _descripcion = 'CO tipo medio'

    _columns = {

        'nombre': fields.char('nombre medio'),
               
    }        

tipo_medio()
