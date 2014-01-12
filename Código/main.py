/*

  Esta archivo pertenece a la aplicación "practica 3" bajo licencia GPLv2.
  Copyright (C) 2014 Jaime Torres Benavente.

  Este programa es software libre. Puede redistribuirlo y/o modificarlo bajo los términos 
  de la Licencia Pública General de GNU según es publicada por la Free Software Foundation, 
  bien de la versión 2 de dicha Licencia o bien (según su elección) de cualquier versión 
  posterior.

  Este programa se distribuye con la esperanza de que sea útil, pero SIN NINGUNA GARANTÍA, 
  incluso sin la garantía MERCANTIL implícita o sin garantizar la CONVENIENCIA PARA UN 
  PROPÓSITO PARTICULAR. Véase la Licencia Pública General de GNU para más detalles.

  Debería haber recibido una copia de la Licencia Pública General junto con este programa. 
  Si no ha sido así, escriba a la Free Software Foundation, Inc., en 675 Mass Ave, Cambridge, 
  MA 02139, EEUU.

*/


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
