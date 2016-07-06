import csv
with open("backend/frontend/map/Salmonella_Distances_Bray_Curtis.csv", "r") as f:
    reader = csv.DictReader(f)
    entries = {}
    for row in reader:
        for item in row.items():
            if item[0] == '':
                continue
            else:
                index = item[0].split('2')
                country = index[0]
                year = int('2' + index[1])
        if year in year:
            entries[year][country] = item[1]
        else:
            entries[year] = {country: item[1]}
