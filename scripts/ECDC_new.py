import csv
import json
with open("scripts/isocountries.json", "r") as g:
    countries = json.load(g)
    with open("attr_data/ECDC.csv", "rU") as f:
        reader = csv.DictReader(f)
        data = []
        for row in reader:
            for i in countries:
                if i['name'] == row['Country']:
                    country = i['alpha3']
                    break
            row['id'] = country
            new_entry = {}
            for j in row:
                new_entry[j] = row[j].decode('latin-1')
            data.append(new_entry)
    print json.dumps(data)
    # for i in data:
    #     print i['id']
    # print data
        # print row
            # for item in row.items():
            #     if item[0] == '':
            #         continue
            #     else:
            #         index = item[0].split('2')
            #         country = index[0]
            #         year = int('2' + index[1])
            # if year in year:
            #     entries[year][country] = item[1]
            # else:
            #     entries[year] = {country: item[1]}
