# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 12:07:52 2013

@author: jaime
"""


from cafe import *
from tiposCafes import *
from gestion import *
from contacto import *
import web
import tempfile

web.config.debug=False
             
urls = (
    '/cafe', 'Cafe', #
    '/cafe/form','Cafe_f',
    '/cafe/gestion','Gestion',
    '/cafe/gestion_actualizar','Actualizar',
    '/cafe/gestion_borrar','Borrar',
    '/cafe/cerrarsesion','Cafe_cerrarS',
    '/cafe/Cafe1','Cafe1',
    '/cafe/Cafe2','Cafe2',
    '/cafe/Cafe3','Cafe3',
    '/cafe/Cafe4','Cafe4',
    '/cafe/contacto','Contacto'
)



app = web.application(urls, globals())

session=web.session.Session(app,web.session.DiskStore(tempfile.mkdtemp()))

def session_hook():
	web.ctx.session=session

# Gestionamos el error 404 (not found)
def notfound():
    return web.notfound("Lo siento, la p&aacute;gina que buscas no existe")

app.add_processor(web.loadhook(session_hook))

# Asignamos el gestor del not found de la aplicación web a la función anterior
app.notfound = notfound

if __name__ == "__main__":
    app.run()