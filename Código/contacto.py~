# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 13:07:55 2013

@author: jaime
"""
import web
from web.contrib.template import render_mako
from web import form

import pymongo
import feedparser
import time
from keys import *
import tweepy

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

def actualiza_tweet():
    conn=pymongo.MongoClient()
    db=conn.mydb
    cache=db.cache
    tiempo1=time.time()
    t=cache.find_one({"rss":"tweet"})
    tiempo2=t[u'ult_act']

    if((tiempo2- tiempo1)>600):
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
        api = tweepy.API(auth)
        result = api.user_timeline("torresjTIC")
        tweet=[]
        for status in result:
            geo=status.geo
            if geo!=None:
                tweet.append([status.text,[geo[u'coordinates'][0],geo[u'coordinates'][1]]])
        cache.update({"rss": "tweet"}, {"$set": {"ult_act": time.time()}})
        

    conn.close() 


#Variable para RSS, también almacenamos el momento en que se descargo el rss
rss=feedparser.parse('http://ep00.epimg.net/rss/tags/ultimas_noticias.xml')
actualiza_tiempo()

#Conectamos con tweeter para obtener los twits
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
result = api.user_timeline("torresjTIC")
tweet=[]
for status in result:
    geo=status.geo
    if geo!=None:
        print status.text
        tweet.append([status.text,[geo[u'coordinates'][0],geo[u'coordinates'][1]]])

actualiza_tweet()


# funciones para usar como listas de dias meses y años
def dias():
    x=[];
    for n in range(1,32):
        x.append(n)
    return x
    
def meses():
    x=[];
    for n in range(1,13):
        x.append(n)
    return x   

def anios():
    x=[];
    for n in range(1940,2014):
        x.append(n)
    return x

meses31=['1','3','4','7','8','10','12']
meses30=['5','6','9','11']

#Validadores
vpass=form.regexp(r'.{7,20}$',"La contrasenia debe tener mas de 7 caracteres")
vemail=form.regexp(r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}\b',"Introduzca una direccion de correo valida")

#Formulario Para el login
formul = form.Form( 
    form.Textbox("user",form.notnull,description = "Usuario:"),
    form.Password("password",form.notnull,vpass,description = "Contraseña:"),
    form.Button("Login")
)



class Contacto:
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
        registro=0
        titulo="CAFE DEL MAR"
        subtitulo1="Oferta de cafes"
        cafes=[["Cafe1","Descripcion del cafe 1"],["Cafe2","Descripcion del cafe 2"],["Cafe3","Descripcion del cafe 3"],["Cafe4","Descripcion del cafe 4"]]
        cafeEspecial=["Cafe especial de la casa","Descripcion cafe especial de la casa"]
        piepagina="Copyright &copy; 2013 Jaime Torres Benavente"
        subtitulo2="Localizacion"
        cuerpo="Cuerpoooooooooooooooooooooo"
        subtitulo3=""
        subtitulo4=""
        servicios=[]
        reg=False
        modo="contacto"
        error=''
        actualiza_tiempo()
        actualiza_tweet()
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
            rss=rss,
            tweet=tweet)

    def POST(self): 
        login=formul()
        registro=0
        titulo="CAFE DEL MAR"
        subtitulo1="Oferta de cafes"
        cafes=[["Cafe1","Descripcion del cafe 1"],["Cafe2","Descripcion del cafe 2"],["Cafe3","Descripcion del cafe 3"],["Cafe4","Descripcion del cafe 4"]]
        cafeEspecial=["Cafe especial de la casa","Descripcion cafe especial de la casa"]
        piepagina="Copyright &copy; 2013 Jaime Torres Benavente"
        subtitulo2="Localizacion"
        cuerpo="Cuerpo00oooooo"
        subtitulo3=""
        subtitulo4=""
        servicios=[]
        reg=False
        modo="contacto"
        error=''
        actualiza_tiempo()
        actualiza_tweet()
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
            rss=rss,
            tweet=tweet)

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
            rss=rss,
            tweet=tweet)