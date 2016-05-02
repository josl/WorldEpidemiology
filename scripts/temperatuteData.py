#!/usr/bin/env python2.7

import csv
import os
import openpyxl
import re
import json
import sys
import pickle
import pprint
import pandas
from pymongo import MongoClient

# client = MongoClient('mongodb://192.168.99.100:5999/')
data = json.load(pickle.load(open('attr_data/WDI/Bram/NAOO/TemperatureData.json')))

for i in data:
    print i

# db = client['topodb']
# collection = db.WDI
# mongo_data = []
# for country in data:
#     for year in data[country]:
#         entry = {}
#         entry['id'] = country
#         try:
#             entry['name'] = [i for i in country_code if country_code[i] == country][0]
#         except:
#             continue
#         entry['date'] = year
#         entry['attrs'] = {}
#         for attr in data[country][year]:
#             new_attr = attr.replace('.', '-')
#             sys.stdout.write('Country: ' + entry['id'] + ' # '+ attr + '\r')
#             entry['attrs'][new_attr] = data[country][year][attr]
#         mongo_data.append(entry)
#         # Push to mongodb!
#         # collection.insert_one(entry)
#
# g = open('attr_data/WDI/WDI_csv/WDIJSON.json', 'w')
# g.write(json.dumps(mongo_data))
# g.close()
