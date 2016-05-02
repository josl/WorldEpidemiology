#!/usr/bin/env python2.7

import csv
import os
import openpyxl
import re
import json
import sys
import pickle
import pprint
from pymongo import MongoClient
import pprint
from sets import Set
import urllib2
import urllib

url = 'http://dataplusapi.icao.int/dataplus/formB/basic?'

'year[]=2016&'
'year[]=2015&'
'filterNames[]=year&'
'dimension[]=from+City&'
'dimension[]=to+City&'
'dimension[]=year&'
'dimension[]=quarter&'
'_search=false&'
'nd=1461909590696'
'&rows=20'
'&page=1'
'&sidx=from+City'
'&sord=asc'

# year[]:2016
# year[]:2015
# year[]:2014
# year[]:2013
# year[]:2012
# year[]:2011
# year[]:2010
# year[]:2009
# year[]:2008
# year[]:2007
# year[]:2006
# year[]:2005
# year[]:2004
# year[]:2003
# year[]:2002
# year[]:2001
# year[]:2000
# year[]:1999
# year[]:1998
# year[]:1997
# year[]:1996
# year[]:1995
# year[]:1994
# year[]:1993
# year[]:1992
# year[]:1991
# year[]:1990
# year[]:1989
# year[]:1988
# year[]:1987
# year[]:1986
# year[]:1985
# year[]:1984
# year[]:1983
# year[]:1982
# airCarrierId[]:120336
# airCarrierId[]:120338
# airCarrierId[]:120736
# airCarrierId[]:120519
# airCarrierId[]:15093453
# airCarrierId[]:120442
# airCarrierId[]:120443
# airCarrierId[]:120342
# airCarrierId[]:120201
# airCarrierId[]:19505932
# airCarrierId[]:120347
# airCarrierId[]:8178807
# airCarrierId[]:120444
# airCarrierId[]:120445
# airCarrierId[]:120520
# airCarrierId[]:120446
# airCarrierId[]:120621
# airCarrierId[]:120623
# airCarrierId[]:120521
# airCarrierId[]:120358
# airCarrierId[]:120447
# airCarrierId[]:8714755
# airCarrierId[]:121277
# airCarrierId[]:120449
# airCarrierId[]:120450
# airCarrierId[]:120776
# airCarrierId[]:120263
# airCarrierId[]:121317
# airCarrierId[]:120626
# airCarrierId[]:121324
# airCarrierStateId[]:10614
# airCarrierStateId[]:10637
# airCarrierStateId[]:10763
# airCarrierStateId[]:10643
# airCarrierStateId[]:10603
# airCarrierStateId[]:10663
# airCarrierStateId[]:10621
# airCarrierStateId[]:10696
# filterNames[]:year
# filterNames[]:airCarrierId
# filterNames[]:airCarrierStateId
# dimension[]:from City
# dimension[]:to City
# dimension[]:year
# dimension[]:quarter
# quarter[]:Q1
# quarter[]:Q2
# quarter[]:Q3
# quarter[]:Q4
# _search:false
# nd:1462201101438
# rows:20
# page:1
# sidx:from City
# sord:asc

# http://dataplusapi.icao.int/dataplus/formB/basic?year%5B%5D=2016&year%5B%5D=2015&year%5B%5D=2014&year%5B%5D=2013&year%5B%5D=2012&year%5B%5D=2011&year%5B%5D=2010&year%5B%5D=2009&year%5B%5D=2008&year%5B%5D=2007&year%5B%5D=2006&year%5B%5D=2005&year%5B%5D=2004&year%5B%5D=2003&year%5B%5D=2002&year%5B%5D=2001&year%5B%5D=2000&year%5B%5D=1999&year%5B%5D=1998&year%5B%5D=1997&year%5B%5D=1996&year%5B%5D=1995&year%5B%5D=1994&year%5B%5D=1993&year%5B%5D=1992&year%5B%5D=1991&year%5B%5D=1990&year%5B%5D=1989&year%5B%5D=1988&year%5B%5D=1987&year%5B%5D=1986&year%5B%5D=1985&year%5B%5D=1984&year%5B%5D=1983&year%5B%5D=1982&airCarrierId%5B%5D=120336&airCarrierId%5B%5D=120338&airCarrierId%5B%5D=120736&airCarrierId%5B%5D=120519&airCarrierId%5B%5D=15093453&airCarrierId%5B%5D=120442&airCarrierId%5B%5D=120443&airCarrierId%5B%5D=120342&airCarrierId%5B%5D=120201&airCarrierId%5B%5D=19505932&airCarrierId%5B%5D=120347&airCarrierId%5B%5D=8178807&airCarrierId%5B%5D=120444&airCarrierId%5B%5D=120445&airCarrierId%5B%5D=120520&airCarrierId%5B%5D=120446&airCarrierId%5B%5D=120621&airCarrierId%5B%5D=120623&airCarrierId%5B%5D=120521&airCarrierId%5B%5D=120358&airCarrierId%5B%5D=120447&airCarrierId%5B%5D=8714755&airCarrierId%5B%5D=121277&airCarrierId%5B%5D=120449&airCarrierId%5B%5D=120450&airCarrierId%5B%5D=120776&airCarrierId%5B%5D=120263&airCarrierId%5B%5D=121317&airCarrierId%5B%5D=120626&airCarrierId%5B%5D=121324&airCarrierStateId%5B%5D=10614&airCarrierStateId%5B%5D=10637&airCarrierStateId%5B%5D=10763&airCarrierStateId%5B%5D=10643&airCarrierStateId%5B%5D=10603&airCarrierStateId%5B%5D=10663&airCarrierStateId%5B%5D=10621&airCarrierStateId%5B%5D=10696&filterNames%5B%5D=year&filterNames%5B%5D=airCarrierId&filterNames%5B%5D=airCarrierStateId&dimension%5B%5D=from+City&dimension%5B%5D=to+City&dimension%5B%5D=year&dimension%5B%5D=quarter&quarter%5B%5D=Q1&quarter%5B%5D=Q2&quarter%5B%5D=Q3&quarter%5B%5D=Q4&_search=false&nd=1462201101438&rows=20&page=1&sidx=from+City&sord=asc

values = {
    'year' : 2016,
    'year' : 'Northampton',
    'language' : 'Python'
}

data = urllib.urlencode(values)
req = urllib2.Request(url, data)
response = urllib2.urlopen(req)
json_data = response.read()
