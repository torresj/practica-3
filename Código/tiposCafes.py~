# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 12:07:52 2013

@author: jaime
"""

import web
from web.contrib.template import render_mako
from web import form

import pymongo
import feedparser
import time

render = render_mako(
        directories=['plantillas'],
        input_encoding='utf-8',
        output_encoding='utf-8',
        )


'''
Esta funcion sirve para actualizar el tiempo del ultimo
acceso al rss, si fuera necesario. Comprobara si han pasado
mas de 10 minutos desde la ultima vez, y si es asi, volverá
a descargar el rss
'''
def actualiza_tiempo():
    conn=pymongo.MongoClient()
    db=conn.mydb
    cache=db.cache
    tiempo1=time.time()
    t=cache.find_one({"rss":"el pais"})
    tiempo2=t[u'ult_act']

    if((tiempo2- tiempo1)>600): 
        cache.update({"rss": "el pais"}, {"$set": {"ult_act": time.time()}})
        rss=feedparser.parse('http://ep00.epimg.net/rss/tags/ultimas_noticias.xml')

    conn.close()   

#Variable para RSS, también almacenamos el momento en que se descargo el rss
rss=feedparser.parse('http://ep00.epimg.net/rss/tags/ultimas_noticias.xml')
actualiza_tiempo()

#Validadores
vpass=form.regexp(r'.{7,20}$',"La contrasenia debe tener mas de 7 caracteres")

#Formulario Para el login
formul = form.Form( 
    form.Textbox("user",form.notnull,description = "Usuario:"),
    form.Password("password",form.notnull,vpass,description = "Contraseña:"),
    form.Button("Login")
)

#Clases para manejar las paginas de los tipos de cafes
class Cafe1:
    def GET(self):
        s=web.ctx.session
        try:
            if s.usuario!='':
                log=True
                user=s.usuario
            else:
                log=False
                user=''
        except AttributeError:
            s.usuario=''
            log=False
            user=''
        
        #Variables para rellenar la pagina web
        login=formul()
        registro=""
        titulo="CAFE DEL MAR"
        subtitulo1="Oferta de cafes"
        cafes=[["Cafe1","Descripcion del cafe 1"],["Cafe2","Descripcion del cafe 2"],["Cafe3","Descripcion del cafe 3"],["Cafe4","Descripcion del cafe 4"]]
        cafeEspecial=["Cafe especial de la casa","Descripcion cafe especial de la casa"]
        piepagina="Copyright &copy; 2013 Jaime Torres Benavente"
        subtitulo2="Cafe 1"
        cuerpo="Descripcion detallada del cafe 1"
        subtitulo3=""
        subtitulo4=""
        servicios=[]
        reg=False
        modo="index"
        error=''
        actualiza_tiempo()
        return render.plantilla(
            titulo=titulo,
            login=login,
            log=log,
            user=user,
            subtitulo1=subtitulo1,
            cafes=cafes,
            cafeEspecial=cafeEspecial,
            subtitulo2=subtitulo2,
            cuerpo=cuerpo,
            registro=registro,
            subtitulo3=subtitulo3,
            subtitulo4=subtitulo4,
            servicios=servicios,
            piepagina=piepagina,
            reg=reg,
            modo=modo,
            error=error,
            rss=rss)


    def POST(self): 
        login=formul()
        registro=""
        titulo="CAFE DEL MAR"
        subtitulo1="Oferta de cafes"
        cafes=[["Cafe1","Descripcion del cafe 1"],["Cafe2","Descripcion del cafe 2"],["Cafe3","Descripcion del cafe 3"],["Cafe4","Descripcion del cafe 4"]]
        cafeEspecial=["Cafe especial de la casa","Descripcion cafe especial de la casa"]
        piepagina="Copyright &copy; 2013 Jaime Torres Benavente"
        subtitulo2="Cafe 1"
        cuerpo="Descripcion del cafe 1"
        subtitulo3=""
        subtitulo4=""
        servicios=[]
        reg=False
        error=''
        modo="index"

        if not login.validates():
            log=False
            user=''
            return render.plantilla(
            titulo=titulo,
            login=login,
            log=log,
            user=user,
            subtitulo1=subtitulo1,
            cafes=cafes,
            cafeEspecial=cafeEspecial,
            subtitulo2=subtitulo2,
            cuerpo=cuerpo,
            registro=registro,
            subtitulo3=subtitulo3,
            subtitulo4=subtitulo4,
            servicios=servicios,
            piepagina=piepagina,
            reg=reg,
            modo=modo,
            error=error,
            rss=rss)

        else:
            s=web.ctx.session

            #buscamos al usuario en la base de datos
            conn=pymongo.MongoClient()
            db=conn.mydb
            usuarios=db.usuarios
            us=usuarios.find_one({"user":login['user'].value})
            conn.close()
            try:
                if login['password'].value==us[u'pass']:
                    log=True
                    user=login['user'].value
                    s.usuario=user
                else:
                    log=False
                    user=''
                    error='contras&ntilde;a erronea'
            except TypeError:
                log=False;
                user=''
                error='El usuario no existe'
            return render.plantilla(
            titulo=titulo,
            login=login,
            log=log,
            user=user,
            subtitulo1=subtitulo1,
            cafes=cafes,
            cafeEspecial=cafeEspecial,
            subtitulo2=subtitulo2,
            cuerpo=cuerpo,
            registro=registro,
            subtitulo3=subtitulo3,
            subtitulo4=subtitulo4,
            servicios=servicios,
            piepagina=piepagina,
            reg=reg,
            modo=modo,
            error=error,
            rss=rss)

class Cafe2:
    def GET(self):
        s=web.ctx.session
        try:
            if s.usuario!='':
                log=True
                user=s.usuario
            else:
                log=False
                user=''
        except AttributeError:
            s.usuario=''
            log=False
            user=''
        
        #Variables para rellenar la pagina web
        login=formul()
        registro=""
        titulo="CAFE DEL MAR"
        subtitulo1="Oferta de cafes"
        cafes=[["Cafe1","Descripcion del cafe 1"],["Cafe2","Descripcion del cafe 2"],["Cafe3","Descripcion del cafe 3"],["Cafe4","Descripcion del cafe 4"]]
        cafeEspecial=["Cafe especial de la casa","Descripcion cafe especial de la casa"]
        piepagina="Copyright &copy; 2013 Jaime Torres Benavente"
        subtitulo2="Cafe 2"
        cuerpo="Descripcion detallada del cafe 2"
        subtitulo3=""
        subtitulo4=""
        servicios=[]
        reg=False
        error=''
        modo="index"
        actualiza_tiempo()
        return render.plantilla(
            titulo=titulo,
            login=login,
            log=log,
            user=user,
            subtitulo1=subtitulo1,
            cafes=cafes,
            cafeEspecial=cafeEspecial,
            subtitulo2=subtitulo2,
            cuerpo=cuerpo,
            registro=registro,
            subtitulo3=subtitulo3,
            subtitulo4=subtitulo4,
            servicios=servicios,
            piepagina=piepagina,
            reg=reg,
            modo=modo,
            error=error,
            rss=rss)


    def POST(self): 
        login=formul()
        registro=""
        titulo="CAFE DEL MAR"
        subtitulo1="Oferta de cafes"
        cafes=[["Cafe1","Descripcion del cafe 1"],["Cafe2","Descripcion del cafe 2"],["Cafe3","Descripcion del cafe 3"],["Cafe4","Descripcion del cafe 4"]]
        cafeEspecial=["Cafe especial de la casa","Descripcion cafe especial de la casa"]
        piepagina="Copyright &copy; 2013 Jaime Torres Benavente"
        subtitulo2="Cafe 2"
        cuerpo="Descripcion del cafe 2"
        subtitulo3=""
        subtitulo4=""
        servicios=[]
        reg=False
        error=''
        modo="index"

        if not login.validates():
            log=False
            user=''
            return render.plantilla(
            titulo=titulo,
            login=login,
            log=log,
            user=user,
            subtitulo1=subtitulo1,
            cafes=cafes,
            cafeEspecial=cafeEspecial,
            subtitulo2=subtitulo2,
            cuerpo=cuerpo,
            registro=registro,
            subtitulo3=subtitulo3,
            subtitulo4=subtitulo4,
            servicios=servicios,
            piepagina=piepagina,
            reg=reg,
            modo=modo,
            error=error,
            rss=rss)

        else:
            s=web.ctx.session

            #buscamos al usuario en la base de datos
            conn=pymongo.MongoClient()
            db=conn.mydb
            usuarios=db.usuarios
            us=usuarios.find_one({"user":login['user'].value})
            conn.close()
            try:
                if login['password'].value==us[u'pass']:
                    log=True
                    user=login['user'].value
                    s.usuario=user
                else:
                    log=False
                    user=''
                    error='contras&ntilde;a erronea'
            except TypeError:
                log=False;
                user=''
                error='El usuario no existe'
            return render.plantilla(
            titulo=titulo,
            login=login,
            log=log,
            user=user,
            subtitulo1=subtitulo1,
            cafes=cafes,
            cafeEspecial=cafeEspecial,
            subtitulo2=subtitulo2,
            cuerpo=cuerpo,
            registro=registro,
            subtitulo3=subtitulo3,
            subtitulo4=subtitulo4,
            servicios=servicios,
            piepagina=piepagina,
            reg=reg,
            modo=modo,
            error=error,
            rss=rss)

class Cafe3:
    def GET(self):
        s=web.ctx.session
        try:
            if s.usuario!='':
                log=True
                user=s.usuario
            else:
                log=False
                user=''
        except AttributeError:
            s.usuario=''
            log=False
            user=''
        
        #Variables para rellenar la pagina web
        login=formul()
        registro=""
        titulo="CAFE DEL MAR"
        subtitulo1="Oferta de cafes"
        cafes=[["Cafe1","Descripcion del cafe 1"],["Cafe2","Descripcion del cafe 2"],["Cafe3","Descripcion del cafe 3"],["Cafe4","Descripcion del cafe 4"]]
        cafeEspecial=["Cafe especial de la casa","Descripcion cafe especial de la casa"]
        piepagina="Copyright &copy; 2013 Jaime Torres Benavente"
        subtitulo2="Cafe 1"
        cuerpo="Descripcion detallada del cafe 3"
        subtitulo3=""
        subtitulo4=""
        servicios=[]
        reg=False
        error=''
        modo="index"
        actualiza_tiempo()
        return render.plantilla(
            titulo=titulo,
            login=login,
            log=log,
            user=user,
            subtitulo1=subtitulo1,
            cafes=cafes,
            cafeEspecial=cafeEspecial,
            subtitulo2=subtitulo2,
            cuerpo=cuerpo,
            registro=registro,
            subtitulo3=subtitulo3,
            subtitulo4=subtitulo4,
            servicios=servicios,
            piepagina=piepagina,
            reg=reg,
            modo=modo,
            error=error,
            rss=rss)


    def POST(self): 
        login=formul()
        registro=""
        titulo="CAFE DEL MAR"
        subtitulo1="Oferta de cafes"
        cafes=[["Cafe1","Descripcion del cafe 1"],["Cafe2","Descripcion del cafe 2"],["Cafe3","Descripcion del cafe 3"],["Cafe4","Descripcion del cafe 4"]]
        cafeEspecial=["Cafe especial de la casa","Descripcion cafe especial de la casa"]
        piepagina="Copyright &copy; 2013 Jaime Torres Benavente"
        subtitulo2="Cafe 3"
        cuerpo="Descripcion del cafe 3"
        subtitulo3=""
        subtitulo4=""
        servicios=[]
        reg=False
        error=''
        modo="index"

        if not login.validates():
            log=False
            user=''
            return render.plantilla(
            titulo=titulo,
            login=login,
            log=log,
            user=user,
            subtitulo1=subtitulo1,
            cafes=cafes,
            cafeEspecial=cafeEspecial,
            subtitulo2=subtitulo2,
            cuerpo=cuerpo,
            registro=registro,
            subtitulo3=subtitulo3,
            subtitulo4=subtitulo4,
            servicios=servicios,
            piepagina=piepagina,
            reg=reg,
            modo=modo,
            error=error,
            rss=rss)

        else:
            s=web.ctx.session

            #buscamos al usuario en la base de datos
            conn=pymongo.MongoClient()
            db=conn.mydb
            usuarios=db.usuarios
            us=usuarios.find_one({"user":login['user'].value})
            conn.close()
            try:
                if login['password'].value==us[u'pass']:
                    log=True
                    user=login['user'].value
                    s.usuario=user
                else:
                    log=False
                    user=''
                    error='contras&ntilde;a erronea'
            except TypeError:
                log=False;
                user=''
                error='El usuario no existe'
            return render.plantilla(
            titulo=titulo,
            login=login,
            log=log,
            user=user,
            subtitulo1=subtitulo1,
            cafes=cafes,
            cafeEspecial=cafeEspecial,
            subtitulo2=subtitulo2,
            cuerpo=cuerpo,
            registro=registro,
            subtitulo3=subtitulo3,
            subtitulo4=subtitulo4,
            servicios=servicios,
            piepagina=piepagina,
            reg=reg,
            modo=modo,
            error=error,
            rss=rss)

class Cafe4:
    def GET(self):
        s=web.ctx.session
        try:
            if s.usuario!='':
                log=True
                user=s.usuario
            else:
                log=False
                user=''
        except AttributeError:
            s.usuario=''
            log=False
            user=''
        
        #Variables para rellenar la pagina web
        login=formul()
        registro=""
        titulo="CAFE DEL MAR"
        subtitulo1="Oferta de cafes"
        cafes=[["Cafe1","Descripcion del cafe 1"],["Cafe2","Descripcion del cafe 2"],["Cafe3","Descripcion del cafe 3"],["Cafe4","Descripcion del cafe 4"]]
        cafeEspecial=["Cafe especial de la casa","Descripcion cafe especial de la casa"]
        piepagina="Copyright &copy; 2013 Jaime Torres Benavente"
        subtitulo2="Cafe 4"
        cuerpo="Descripcion detallada del cafe 4"
        subtitulo3=""
        subtitulo4=""
        servicios=[]
        reg=False
        error=''
        modo="index"
        actualiza_tiempo()
        return render.plantilla(
            titulo=titulo,
            login=login,
            log=log,
            user=user,
            subtitulo1=subtitulo1,
            cafes=cafes,
            cafeEspecial=cafeEspecial,
            subtitulo2=subtitulo2,
            cuerpo=cuerpo,
            registro=registro,
            subtitulo3=subtitulo3,
            subtitulo4=subtitulo4,
            servicios=servicios,
            piepagina=piepagina,
            reg=reg,
            modo=modo,
            error=error,
            rss=rss)


    def POST(self): 
        login=formul()
        registro=""
        titulo="CAFE DEL MAR"
        subtitulo1="Oferta de cafes"
        cafes=[["Cafe1","Descripcion del cafe 1"],["Cafe2","Descripcion del cafe 2"],["Cafe3","Descripcion del cafe 3"],["Cafe4","Descripcion del cafe 4"]]
        cafeEspecial=["Cafe especial de la casa","Descripcion cafe especial de la casa"]
        piepagina="Copyright &copy; 2013 Jaime Torres Benavente"
        subtitulo2="Cafe 4"
        cuerpo="Descripcion del cafe 4"
        subtitulo3=""
        subtitulo4=""
        servicios=[]
        reg=False
        error=''
        modo="index"

        if not login.validates():
            log=False
            user=''
            return render.plantilla(
            titulo=titulo,
            login=login,
            log=log,
            user=user,
            subtitulo1=subtitulo1,
            cafes=cafes,
            cafeEspecial=cafeEspecial,
            subtitulo2=subtitulo2,
            cuerpo=cuerpo,
            registro=registro,
            subtitulo3=subtitulo3,
            subtitulo4=subtitulo4,
            servicios=servicios,
            piepagina=piepagina,
            reg=reg,
            modo=modo,
            error=error,
            rss=rss)

        else:
            s=web.ctx.session

            #buscamos al usuario en la base de datos
            conn=pymongo.MongoClient()
            db=conn.mydb
            usuarios=db.usuarios
            us=usuarios.find_one({"user":login['user'].value})
            conn.close()
            try:
                if login['password'].value==us[u'pass']:
                    log=True
                    user=login['user'].value
                    s.usuario=user
                else:
                    log=False
                    user=''
                    error='contras&ntilde;a erronea'
            except TypeError:
                log=False;
                user=''
                error='El usuario no existe'
            return render.plantilla(
            titulo=titulo,
            login=login,
            log=log,
            user=user,
            subtitulo1=subtitulo1,
            cafes=cafes,
            cafeEspecial=cafeEspecial,
            subtitulo2=subtitulo2,
            cuerpo=cuerpo,
            registro=registro,
            subtitulo3=subtitulo3,
            subtitulo4=subtitulo4,
            servicios=servicios,
            piepagina=piepagina,
            reg=reg,
            modo=modo,
            error=error,
            rss=rss)



