##############################
#Name: Load_games_mongo
#
#Goals: Load BGG game into a mongoDB 
#
#Args: None
###############################


# Import Libraries

import requests as rq
import time 
import json
import pandas as pd
import sys
import pymongo
import json
import xmltodict
from pymongo import MongoClient

# MongoDB connections 
mongodb = MongoClient('localhost', 27017)



# Load Data 

for i in range(1,50000):
    
    
    uri = 'http://www.boardgamegeek.com/xmlapi2/thing?id='+str(i)+'&type=boardgame,boardgameexpansion'
    
    while True:
        bgg_user_get = rq.get(uri)
        if (bgg_user_get.status_code == 200):
            break
        time.sleep(1)
    
    
    
    #print bgg_user_get.text
    bgg_user = xmltodict.parse(bgg_user_get.text.encode('utf-8'))
    bgg_user['_id']=i
    time.sleep(1)
    mongodb.bgg.boardgames.insert_one(bgg_user)