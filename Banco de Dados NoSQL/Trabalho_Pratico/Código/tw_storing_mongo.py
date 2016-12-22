import tweepy
import pymongo
import json
import time
import os

from pymongo import MongoClient

from tweepy.streaming import StreamListener
from tweepy.auth import OAuthHandler
from tweepy import Stream

consumer_key= ""
consumer_secret= ""
access_token= ""
access_token_secret= ""

#grabs the system time
#start_time = time.time()

#track list
#keyword_list = ['twitter']

#Creates an OAuthHandler instance to handle OAuth credentials
#Creates a listener instance with a start time and time parameters passed to it
#Creates an StreamListener instance with the OAuthHandler instance and the listener instance
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

## MODIFICAR ESSA PARTE
#public_tweets = api.home_timeline()
#for tweet in public_tweets:
#    print (tweet.text)

class MyListener(StreamListener):

        def on_data(self, data):
                try:
                        with open('python.json', 'a') as f:
                                f.write(data)
                                return True
                        
                        except BaseException as e:
                                print str(e)
                                return True
       def on_error(self, status):
              print(status)
              return True
        
twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#python'])
                



  


