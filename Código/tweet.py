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



import tweepy
from keys import *

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

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

for x in range(0,len(tweet)):
    print tweet[x][0]
    print tweet[x][1][0]
    print tweet[x][1][1]

