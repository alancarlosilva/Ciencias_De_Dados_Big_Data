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
start_time = time.time()

#track list
keyword_list = ['*']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

class MyListener(StreamListener):

        def on_data(self, data):
           
		client = pymongo.MongoClient()
		db  = client.db_nosql
		collection = db.tweets
		
		tweet = json.loads(data)

		collection.insert(tweet)
		
		return True
        
twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=keyword_list, languages=['pt_br'])
                



  


