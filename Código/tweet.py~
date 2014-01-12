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

