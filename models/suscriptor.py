# -*- coding: utsuscriptorfrom openerp.suscriptort osv, fields

class suscriptor(osv.osv):
    _name = 'co.suscriptor'
    _description = 'Clase que contiene los elementos definidos de negocio para el suscriptor'
    
    _columnas = {
        'nombre': fields.char('Nombre y Apellido'),
        'identificacion': fields.char('Cédula'),
        'direccion': fields.text('Dirección'),
    }

suscriptor()


        