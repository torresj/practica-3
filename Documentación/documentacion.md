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

# PRÁCTICA 3 : Diseño de máquinas virtuales

En esta tercera práctica vamos a configurar una maquina virtual para que sea un servidor web
para un aplicación. Esta maquina virtual deberá ser lo mas adecuada posible para el proposito
que va a desempeñar por lo que voy a probar varios sistemas operativos, locales y en la nube,
y además intentaré encontrar la configuración de recursos mas adecuada.


## Aplicación Web

Siguiendo la línea de las anteriores practicas, voy a montar un servidor web con web.py para
una página web en python que usa algunos servicios de google y que necesita una base de datos
mongoDB. Como tampoco es el objetivo de la practica, no voy a comentar nada de esta aplicación
salvo para comparar resultados entre las distintas configuraciones.

## Configuraciones

Voy a usar dos maquinas virtuales para comparar en azure. CentOS y ubuntu 12.04

### ubuntu 12.04

Voy a usar la aplicacion web de azure ya que es muy intuitiva y simple de usar.
Creamos la maquina virtual siguiendo los pasos y tras unos segundos nos aparecera
en la web de azure.

![captura1](https://dl.dropboxusercontent.com/u/17453375/ubuntu-server-12-04.png)

![captura2](https://dl.dropboxusercontent.com/u/17453375/ubuntu-server-12-04-2.png)

![captura3](https://dl.dropboxusercontent.com/u/17453375/ubuntu-server-12-04-3.png)


Ahora ya podemos acceder a la maquina virtual con ssh.

    ssh jaime@iv-ubuntu-1204.cloudapp.net 

![captura5](https://dl.dropboxusercontent.com/u/17453375/ssh-azure-ubuntu1204.png)

Una vez dentro necesitamos instalar una serie de paquetes para que la aplicación web
mencionada mas arriba funcione, entre ellas python-dev o build-essential además de
las bibliotecas necesarias de python como web.py o mako.

    sudo apt-get install python-dev
    sudo apt-get install build-essential
    sudo apt-get install git
    sudo apt-get install python-pip
    sudo pip install web.py
    sudo pip install mako
    sudo pip install pymongo
    sudo pip install tweepy
    sudo pip install feedparser

Ahora solo nos queda descargar la base de datos mongoDB para tener la maquina preparada.
Podemos hacer usando ftp o descargandolo directamente en la maquina virtual.

    sftp iv-ubuntu-1204.cloudapp.net
    put mongodb.tar.gz

Tras unos minutos tendremos la base de datos en la maquina virtual ya solo nos quedará
descargar la aplicacion que esta en un repositorio de github, y lanzar tanto la base
de datos como la aplicación

nota: Se puede añadir un puerto para que vaya la aplicacion a traves del 8080 o bien cambiar
en web.py el puerto por defecto.


![captura4](https://dl.dropboxusercontent.com/u/17453375/ubuntu-server-12-04-4.png)

Para que la aplicación funcione aunque cerremos la conexion ssh, podemos usar nohup.

### CentOS

El proceso es exactamente el mismo para centos, seguimos los mismos pasos que antes 
salvo que usamos yum y lo usamos para los paquetes de desarrollo.

    sudo yum update
    sudo yum groupinstall -y "Development tools"
    sudo yum install gcc python-devel

Despues de instalar los paquetes de python y git, podemos descargar la aplicacion,
y pasar por sftp la base de datos mongodb.

    sftp jaime@iv-centos.cloudapp.net
    put mongodb.tar.gz

Lanzamos la base de datos y la aplicacion igual que antes y probamos a acceder desde
el navegador.(La direccion web la obtenemos de la pagina de azure)


![captura6](https://dl.dropboxusercontent.com/u/17453375/centOS.png)


## Benchmarks

Hemos cogido para ambas configuraciones los menores recursos posibles que permite azure
ya que si queremos hacer un uso real, esta aplicacion web no necesita muchos recursos ni
va a tener gran cantidad de visitas, además de esta forma podríamos usar mejor los recursos
permitiendo contener mas maquinas virtuales en una sola maquina real (Usando nuestro PC
por ejemplo)

Simplemente haciendo una rapida busqueda por internet podemos encontrar varios benchmarks para
probar servidores web. Yo he elegido ab y httperf. Instalamos ambos en mi pc local y los 
ejecutamos para cada maquina virtual para posteriormente comparar los resultados.

### AB

Apache benchmarks nos permite realizar muchas peticiones concurrentes a un servidor web para 
medir los tiempos de respuesta. Tal y como se hizo en un ejercicio de temas anteriores, laznamos
el siguiente comando para realizar 1000 peticiones con 100 de concurrencia. La pagina que vamos
a pedir no es la principal, si no la de contacto en la que encontramos el servicio de google maps

![captura7](https://dl.dropboxusercontent.com/u/17453375/cafe-maps.png)



    ab -n 1000 -c 100 -g ubuntu-12-04.txt http://iv-ubuntu-1204.cloudapp.net:8080/cafe/contacto
    ab -n 1000 -c 100 -g centOS.txt http://iv-centos.cloudapp.net:8080/cafe/contacto

Con la opcion -g guardamos los resultados en un archivo para ahora generar las graficas con
gnu-plot

    gnuplot -e 'set terminal png; set output "centOS-grafica.png"; set xlabel "Petición"; 
    set ylabel "ms"; plot "centOS.txt" using 10 with lines title "Tiempo de respuesta"'


    gnuplot -e 'set terminal png; set output "ubuntu-12-04.txt.png"; set xlabel "Petición"; 
    set ylabel "ms"; plot "ubuntu-12-04.txt" using 10 with lines title "Tiempo de respuesta"'

CentOS

![captura7](https://dl.dropboxusercontent.com/u/17453375/centOS-grafica.png)


Ubuntu server

![captura8](https://dl.dropboxusercontent.com/u/17453375/ubuntu-12-04-grafica.png)


### httperf

Ahora vamos a usar httperf y vamos a intentar estresar un poco mas el servidor mandando
mas peticiones por segundo y mas peticiones en total.

    httperf --server 137.117.146.50 --port 8080 --uri /cafe/contacto/ --rate 300 --num-conn 30000 --num-call 1 --timeout 5
    httperf --server 137.117.146.80 --port 8080 --uri /cafe/contacto/ --rate 300 --num-conn 30000 --num-call 1 --timeout 5

| Maquina Virtual | Tiempo de respuesta (ms) |
| --------------- | ------------------------ |
| Ubuntu Server 12.04| 4468.5 |
| CentOS |  1010.5 |


## Conclusiones

A la vista de los resultados podemos ver que en ambos benchmarks centOS esta más optimizado
que ubuntu server 12.04. Tambien vemos que el tiempo de respuesta de media que nos da httperf
de 1 segundo en el caso de centOS, es razonable para el uso de esta aplicación por lo que
no sería necesario tener que amplicar la maquina con mas recursos. En general esta es una
comparación muy pobre ya que sería mas util, ademas de distintas configuraciones, comparar
entre amazon y azure, pero no consegui darme de alta en amazon y opté por probar solo en 
azure. No he probado maquinas locales porque no tendría mucho sentido ya que la velocidad de
respuesta devería ser mas rapida al estar en el mismo equipo y no tener retardo por la red
ni por el propio servicio de azure.

En cuanto a la aplicación, no comento nada ya que tampoco es objetivo de esta practica, 
aunque ambas maquinas estan ejecutandose y pueden ser probadas por cualquier persona en:

* [centOS](http://iv-centos.cloudapp.net:8080/cafe)

* [Ubuntu server 12.04](http://iv-ubuntu-1204.cloudapp.net:8080/cafe)

