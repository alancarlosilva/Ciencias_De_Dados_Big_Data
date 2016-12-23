import pymongo
import datetime
import pprint
import re
import nltk
import bson

from bson.code import Code
from bson.son import SON
from bson.objectid import ObjectId
from pymongo import MongoClient
from nltk.tokenize import word_tokenize

client = pymongo.MongoClient()

db = client.bd_nosql

collection = db.pubs

mapper = Code("""
				function(){
					emit(this._id, this.name);
				};
			""")

reducer = Code("""
				function(key, values){
					var total = 0;
					for (var i = 0; i < values.length; i++){
						total += values[i];
					}
					return total;
				}
			""")

result_pubs = db.pubs.map_reduce(mapper, reducer, "resultado", query = {"name": {"$lt":5}})

for document in result_pubs.find():
	pprint.pprint(document)