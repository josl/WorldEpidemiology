#!/usr/bin/env python2.7

import csv
import os
import openpyxl
import re
import json
import sys
import pickle

path = '../attr_data/WDI'
# Array of 242 elements
elements = (252-4)*(2015-1960+1)
data = []
i = 0
for filename in os.listdir(path):
    if '.' not in filename or filename.split('.')[1] != 'xlsx':
        continue
    wb = openpyxl.load_workbook(path + '/' + filename)
    sheet = wb.get_sheet_by_name('Data')
    date = sheet['B2'].value
    for row in range(5, 253):
        for rowOfCellObjects in sheet['E' + str(row):'BH' + str(row)]:
            id = sheet['B' + str(row)].value
            name = sheet['A' + str(row)].value
            attr = sheet['C' + str(row)].value.replace(' ', '_').replace('.', '_').lower()
            # attr_code = sheet['D' + str(row)].value.replace(' ', '_').replace('.', '_').lower()
            for cellObj in rowOfCellObjects:
                country = {}
                country['id'] = id
                country['name'] = name
                country[attr] = cellObj.value
                # country[attr_code] = {
                #     'value': cellObj.value,
                #     'name': attr
                # }
                out = re.match(r'([A-Z]+)([0-9]+)', cellObj.coordinate)
                country['date'] = sheet[out.group(1) + '4'].value
                if len(data) < elements:
                    sys.stdout.write('Appending: ' + id + ' ' + filename + '\r')
                    # First file, still processing countries and years
                    if cellObj.value:
                        data.append(country)
                else:
                    sys.stdout.write('Next countries: ' + id  + ' ' + filename +  '\r')
                    # Rest of files, find position for country and year
                    for old_country in data:
                        if old_country['id'] == id and old_country['date'] == country['date']:
                            if cellObj.value:
                                country[attr] = cellObj.value
                                # old_country[attr_code] = {
                                #     'value': cellObj.value,
                                #     'name': attr
                                # }
    sys.stdout.write('\n')
    i += 1

# for filename in os.listdir('../attr_data/WDI/blue'):
#     if '.' not in filename or filename.split('.')[1] != 'xltx':
#         continue
#     wb = openpyxl.load_workbook(path + '/' + filename)
#     sheet = wb.get_sheet_by_name('Data')

output = open(path + '/old_attr.pkl', 'wb')

# Pickle dictionary using protocol 0.
pickle.dump(data, output)

g = open(path + '/attr.json', 'w')
g.write(json.dumps(data))
