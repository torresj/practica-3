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

'''def inicializa_tiempo():
    conn=pymongo.MongoClient()
    db=conn.mydb
    cache=db.cache            
    tiempo={
    "rss":"el pais",
    "ult_act":time.time()}
    cache.insert(tiempo)
    conn.close()
'''

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

render = render_mako(
        directories=['plantillas'],
        input_encoding='utf-8',
        output_encoding='utf-8',
        )

#Variable para RSS, también almacenamos el momento en que se descargo el rss
rss=feedparser.parse('http://ep00.epimg.net/rss/tags/ultimas_noticias.xml')
actualiza_tiempo()

#Validadores
vpass=form.regexp(r'.{7,20}$',"La contrasenia debe tener mas de 7 caracteres")
vemail=form.regexp(r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}\b',"Introduzca una direccion de correo valida")

#Formulario Para el login
formul = form.Form( 
    form.Textbox("user",form.notnull,description = "Usuario:"),
    form.Password("password",form.notnull,vpass,description = "Contraseña:"),
    form.Button("Login")
)

#Formulario para el registro

formul2 = form.Form( 
    form.Textbox("nombre",form.notnull,description = "Nombre:"),
    form.Textbox("apellidos",form.notnull, description = "Apellidos:"),
    form.Textbox("email",form.notnull,vemail, description = "Email:"),
    form.Dropdown("dia",dias(),pre="D&iacute;a ",description="Fecha de nacimiento"),
    form.Dropdown("mes",meses(),pre="Mes ",description="Fecha de nacimiento"),
    form.Dropdown("anio",anios(),pre="A&ntilde;o ",description="Fecha de nacimiento"),
    form.Textarea("direccion",form.notnull,description = "Direccion:"),
    form.Textbox("user",form.notnull,description = "Usuario:"),
    form.Password("password",vpass,description = "Contraseña:"),
    form.Password("password2",description = "Repita la contraseña:"),
    form.Checkbox("condiciones",description="Acepto las condiciones",value="on"),
    form.Button("Registrar"),
    validators = [
        form.Validator("No coinciden las contraseña", lambda i: i.password == i.password2),
        form.Validator("Hay que aceptar las condiciones", lambda j: j.condiciones == "on"),
        form.Validator("Fecha incorrecta",lambda k: (k.mes in meses31) or ((k.mes in meses30) and int(k.dia)<31) or ((int(k.mes) == 2) and int(k.dia)<29) or ((int(k.mes) == 2) and int(k.dia)<30 and int(k.anio)%4==0))
        ]
)



#clase para gestionar la página principal
class Cafe:
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
        registro=formul2()
        titulo="CAFE DEL MAR"
        subtitulo1="Oferta de cafes"
        cafes=[["Cafe1","Descripcion del cafe 1"],["Cafe2","Descripcion del cafe 2"],["Cafe3","Descripcion del cafe 3"],["Cafe4","Descripcion del cafe 4"]]
        cafeEspecial=["Cafe especial de la casa","Descripcion cafe especial de la casa"]
        piepagina="Copyright &copy; 2013 Jaime Torres Benavente"
        subtitulo2="Introduccion"
        cuerpo="Cuerpo"
        subtitulo3="Nuestros servicios especiales"
        subtitulo4="Descripcion de los servicios especiales"
        servicios=["Servicio 1","Servicio 2","Servicio 3","Servicio 4"]
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
        registro=formul2()
        titulo="CAFE DEL MAR"
        subtitulo1="Oferta de cafes"
        cafes=[["Cafe1","Descripcion del cafe 1"],["Cafe2","Descripcion del cafe 2"],["Cafe3","Descripcion del cafe 3"],["Cafe4","Descripcion del cafe 4"]]
        cafeEspecial=["Cafe especial de la casa","Descripcion cafe especial de la casa"]
        piepagina="Copyright &copy; 2013 Jaime Torres Benavente"
        subtitulo2="Introduccion"
        cuerpo="Cuerpo"
        subtitulo3="Nuestros servicios especiales"
        subtitulo4="Descripcion de los servicios especiales"
        servicios=["Servicio 1","Servicio 2","Servicio 3","Servicio 4"]
        reg=False
        modo="index"
        error=''
        actualiza_tiempo()
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

#Clase para gestionar la paogina del formulario de registro
class Cafe_f:
    def GET(self):
        #Variables para rellenar la pagina web
        login=formul()
        registro=formul2()
        log=False
        user=''
        titulo="CAFE DEL MAR"
        subtitulo1="Oferta de cafes"
        cafes=[["Cafe1","Descripcion del cafe 1"],["Cafe2","Descripcion del cafe 2"],["Cafe3","Descripcion del cafe 3"],["Cafe4","Descripcion del cafe 4"]]
        cafeEspecial=["Cafe especial de la casa","Descripcion cafe especial de la casa"]
        piepagina="Copyright &copy; 2013 Jaime Torres Benavente"
        subtitulo2="Registro"
        cuerpo=""
        subtitulo3=""
        subtitulo4=""
        servicios=[]
        reg=False
        modo="form"
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
        registro=formul2()
        log=False
        user=''
        titulo="CAFE DEL MAR"
        subtitulo1="Oferta de cafes"
        cafes=[["Cafe1","Descripcion del cafe 1"],["Cafe2","Descripcion del cafe 2"],["Cafe3","Descripcion del cafe 3"],["Cafe4","Descripcion del cafe 4"]]
        cafeEspecial=["Cafe especial de la casa","Descripcion cafe especial de la casa"]
        piepagina="Copyright &copy; 2013 Jaime Torres Benavente"
        subtitulo2="Registro"
        cuerpo=""
        subtitulo3=""
        subtitulo4=""
        servicios=[]
        modo="form"
        error=''
        if not registro.validates():
            reg=False
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
            
            conn=pymongo.MongoClient()
            db=conn.mydb
            usuarios=db.usuarios            
            usuario={
                "user":registro['user'].value,
                "pass":registro['password'].value,
                "nombre":registro['nombre'].value,
                "apellidos":registro['apellidos'].value,
                "dia":registro['dia'].value,
                "mes":registro['mes'].value,
                "anio":registro['anio'].value,
                "email":registro['email'].value,
                "direccion":str(registro['direccion'].value)}
            usuarios.insert(usuario)
            conn.close()

            reg=True
            cuerpo="Usuario registrado con exito"

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


#Clase para cerrar las sesiones
class Cafe_cerrarS:

    def GET(self):
        s=web.ctx.session
        s.kill()
        web.redirect('/cafe')

