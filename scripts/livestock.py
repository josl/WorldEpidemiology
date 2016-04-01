import csv

with open('attr_data/datalivestock.csv', 'wb') as g:
    with open('attr_data/Production_Livestock_E_All_Data.csv', 'r') as f:
        field_names = tuple(f.readline().strip().split(','))
        print field_names
        writer = csv.writer(g, quoting=csv.QUOTE_ALL, delimiter=',')
        writer.writerow(field_names)
        i = 0
        for line in f:
            values = tuple(line.strip().replace('"', '').split(','))
            if i == 0:
                print values
            # print values[1]
            # writer.writerows([values[0], values[1]])
            i += 1
            writer.writerow(values)
