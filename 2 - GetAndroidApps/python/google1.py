import pandas as pd
import itertools

# for scraping app info and reviews from Google Play
from google_play_scraper import app, Sort, reviews

# for pretty printing data structures
from pprint import pprint

# for storing in MongoDB
#import pymongo
#from pymongo import MongoClient

# for keeping track of timing
import datetime as dt
from tzlocal import get_localzone

# for building in wait times
import random
import time

## Read in file containing app names and IDs
app_df = pd.read_csv('apps.csv')
pprint(app_df.head())

## Get list of app names and app IDs
app_names = list(app_df['app_name'])
app_ids = list(app_df['app_id'])

## Loop through app IDs to get app info
app_info = []
for i in app_ids:
    info = app(i)
    del info['comments']
    app_info.append(info)

## Pretty print the data for the first app
#pprint(app_info[0])


pprint(type(app_info))

#d = dict(itertools.zip_longest(*[iter(app_info)] * 2, fillvalue=""))
#pprint(type(d))

df = pd.DataFrame(app_info)
pprint(df.head())

df.to_csv('export1.csv')

