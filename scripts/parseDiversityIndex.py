import csv
import json
data = {}
with open("scripts/isocountries.json", "r") as g:
    countries = json.load(g)
    with open("backend/frontend/map/Salmonella_diversity_indices.csv", "r") as f:
        reader = csv.DictReader(f)
        entries = {}
        for row in reader:
            # if row['alpha'] == 'Inf':
            for i in countries:
                if i['name'] == row['country']:
                    country = i['alpha2']
                    break
            if country in data:
                if int(row['year']) in data[country]:
                    data[country][int(row['year'])][row['alpha']] = float(row['value'])
                else:
                    data[country][int(row['year'])] = {
                        int(row['alpha']): float(row['value'])
                    }
            else:
                data[country] = {
                    int(row['year']): {
                        row['alpha']: float(row['value'])
                    },
                }
        print json.dumps(data)
        # print row
        # for item in row.items():
        #     print item
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
