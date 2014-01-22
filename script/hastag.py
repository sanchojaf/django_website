#!/usr/bin/python
# -*- coding: utf-8 -*-
import tweepy

consumer_key = '9C0Se51B6prF0ZLOabWQ'
consumer_secret = 'QYXmgQAjT4n4gU2Msvre7nPB0i4zXZzhmiLfEN5g'
access_token = '2298854893-LCzkisFl5n60uvoYmm47HCbH0y7YcUVcWIdHYj5' 
access_token_secret = 'FXDzD2AMvf2VmIkjmgYczim6zD1rDxYWKO5lMYHyd3llg'

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
trends1 = api.trends_place(1)

print trends1


trends1 = api.trends_place(1) # from the end of your code
# trends1 is a list with only one element in it, which is a 
# dict which we'll put in data.
data = trends1[0] 

# grab the trends
trends = data['trends']
# grab the name from each trend
names = [trend['name'] for trend in trends]
# put all the names together with a ' ' separating them
trendsName = ' '.join(names)
print(trendsName)
