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

pipeline = [
	#Aqui fazemos o agrupamento de documentos pelo id name e somamos 1 para cada nome igual encontrado
	{"$group": {"_id": "$name", "value": {"$sum": 1}}},
  	
  	#Ordenamos o pipeline anterior  	
  	{"$sort": {"value": -1}},

  	#Limitamos a pesquisa de pubs em 5
  	{"$limit": 5}
]

pprint.pprint(list(collection.aggregate(pipeline)))

	