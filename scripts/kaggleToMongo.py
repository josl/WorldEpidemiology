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

country_code = {
    'Aruba': 'ABW',
    'Andorra': 'AND',
    'Afghanistan': 'AFG',
    'Angola': 'AGO',
    'Anguilla': 'AIA',
    'Albania': 'ALB',
    'Arab World': 'ARB',
    'United Arab Emirates': 'ARE',
    'Argentina': 'ARG',
    'Armenia': 'ARM',
    'American Samoa': 'ASM',
    'Antigua and Barbuda': 'ATG',
    'Australia': 'AUS',
    'Austria': 'AUT',
    'Azerbaijan': 'AZE',
    'Burundi': 'BDI',
    'Belgium': 'BEL',
    'Benin': 'BEN',
    'Burkina Faso': 'BFA',
    'Bangladesh': 'BGD',
    'Bulgaria': 'BGR',
    'Bahrain': 'BHR',
    'Bahamas, The': 'BHS',
    'Bahamas': 'BHS',
    'Bosnia and Herzegovina': 'BIH',
    'Belarus': 'BLR',
    'Belize': 'BLZ',
    'Bermuda': 'BMU',
    'Bolivia': 'BOL',
    'Bolivia (Plurinational State of)': 'BOL',
    'Brazil': 'BRA',
    'Barbados': 'BRB',
    'Brunei Darussalam': 'BRN',
    'Bhutan': 'BTN',
    'Botswana': 'BWA',
    'Central African Republic': 'CAF',
    'Canada': 'CAN',
    'Central Europe and the Baltics': 'CEB',
    'Switzerland': 'CHE',
    'Channel Islands': 'CHI',
    'Chile': 'CHL',
    'China': 'CHN',
    'Cote d\'Ivoire': 'CIV',
    'Cameroon': 'CMR',
    'Congo, Rep.': 'COG',
    'Congo': 'COG',
    'Democratic Republic of the Congo': 'COG',
    'Cook Islands': 'COK',
    'Colombia': 'COL',
    'Comoros': 'COM',
    'Cabo Verde': 'CPV',
    'Costa Rica': 'CRI',
    'Caribbean small states': 'CSS',
    'Cuba': 'CUB',
    'Curacao': 'CUW',
    'Cayman Islands': 'CYM',
    'Cyprus': 'CYP',
    'Czech Republic': 'CZE',
    'Germany': 'DEU',
    'Djibouti': 'DJI',
    'Dominica': 'DMA',
    'Denmark': 'DNK',
    'Dominican Republic': 'DOM',
    'Algeria': 'DZA',
    'East Asia & Pacific (developing only)': 'EAP',
    'East Asia & Pacific (all income levels)': 'EAS',
    'Europe & Central Asia (developing only)': 'ECA',
    'Europe & Central Asia (all income levels)': 'ECS',
    'Ecuador': 'ECU',
    'Egypt, Arab Rep.': 'EGY',
    'Egypt': 'EGY',
    'Euro area': 'EMU',
    'Eritrea': 'ERI',
    'Spain': 'ESP',
    'Estonia': 'EST',
    'Ethiopia': 'ETH',
    'European Union': 'EUU',
    'Fragile and conflict affected situations': 'FCS',
    'Finland': 'FIN',
    'Fiji': 'FJI',
    'France': 'FRA',
    'Faeroe Islands': 'FRO',
    'Micronesia, Fed. Sts.': 'FSM',
    'Micronesia (Federated States of)': 'FSM',
    'Gabon': 'GAB',
    'United Kingdom': 'GBR',
    'United Kingdom of Great Britain and Northern Ireland': 'GBR',
    'Georgia': 'GEO',
    'Ghana': 'GHA',
    'Guinea': 'GIN',
    'Gambia, The': 'GMB',
    'Gambia': 'GMB',
    'Guinea-Bissau': 'GNB',
    'Equatorial Guinea': 'GNQ',
    'Greece': 'GRC',
    'Grenada': 'GRD',
    'Greenland': 'GRL',
    'Guatemala': 'GTM',
    'Guam': 'GUM',
    'Guyana': 'GUY',
    'High income': 'HIC',
    'Hong Kong SAR, China': 'HKG',
    'Honduras': 'HND',
    'Heavily indebted poor countries (HIPC)': 'HPC',
    'Croatia': 'HRV',
    'Haiti': 'HTI',
    'Hungary': 'HUN',
    'Indonesia': 'IDN',
    'Isle of Man': 'IMN',
    'India': 'IND',
    'Not classified': 'INX',
    'Ireland': 'IRL',
    'Iran, Islamic Rep.': 'IRN',
    'Iran (Islamic Republic of)': 'IRN',
    'Iraq': 'IRQ',
    'Iceland': 'ISL',
    'Israel': 'ISR',
    'Italy': 'ITA',
    'Jamaica': 'JAM',
    'Jordan': 'JOR',
    'Japan': 'JPN',
    'Kazakhstan': 'KAZ',
    'Kenya': 'KEN',
    'Kyrgyz Republic': 'KGZ',
    'Kyrgyzstan': 'KGZ',
    'Cambodia': 'KHM',
    'Kiribati': 'KIR',
    'St. Kitts and Nevis': 'KNA',
    'Saint Kitts and Nevis': 'KNA',
    'Korea, Rep.': 'KOR',
    'Republic of Korea': 'KOR',
    'Kosovo': 'KSV',
    'Kuwait': 'KWT',
    'Latin America & Caribbean (developing only)': 'LAC',
    'Lao PDR': 'LAO',
    'Lao People\'s Democratic Republic': 'LAO',
    'Lebanon': 'LBN',
    'Liberia': 'LBR',
    'Libya': 'LBY',
    'St. Lucia': 'LCA',
    'Saint Lucia': 'LCA',
    'Latin America & Caribbean (all income levels)': 'LCN',
    'Least developed countries: UN classification': 'LDC',
    'Low income': 'LIC',
    'Liechtenstein': 'LIE',
    'Sri Lanka': 'LKA',
    'Lower middle income': 'LMC',
    'Low & middle income': 'LMY',
    'Lesotho': 'LSO',
    'Lithuania': 'LTU',
    'Luxembourg': 'LUX',
    'Latvia': 'LVA',
    'Macao SAR, China': 'MAC',
    'St. Martin (French part)': 'MAF',
    'Morocco': 'MAR',
    'Monaco': 'MCO',
    'Moldova': 'MDA',
    'Republic of Moldova': 'MDA',
    'Madagascar': 'MDG',
    'Maldives': 'MDV',
    'Middle East & North Africa (all income levels)': 'MEA',
    'Mexico': 'MEX',
    'Marshall Islands': 'MHL',
    'Middle income': 'MIC',
    'Macedonia, FYR': 'MKD',
    'The former Yugoslav republic of Macedonia': 'MKD',
    'Mali': 'MLI',
    'Malta': 'MLT',
    'Myanmar': 'MMR',
    'Middle East & North Africa (developing only)': 'MNA',
    'Montenegro': 'MNE',
    'Mongolia': 'MNG',
    'Northern Mariana Islands': 'MNP',
    'Mozambique': 'MOZ',
    'Mauritania': 'MRT',
    'Mauritius': 'MUS',
    'Malawi': 'MWI',
    'Malaysia': 'MYS',
    'North America': 'NAC',
    'Namibia': 'NAM',
    'New Caledonia': 'NCL',
    'Niger': 'NER',
    'Nigeria': 'NGA',
    'Nicaragua': 'NIC',
    'Niue': 'NIU',
    'Netherlands': 'NLD',
    'High income: nonOECD': 'NOC',
    'Norway': 'NOR',
    'Nepal': 'NPL',
    'Nauru': 'NRU',
    'New Zealand': 'NZL',
    'High income: OECD': 'OEC',
    'OECD members': 'OED',
    'Oman': 'OMN',
    'Other small states': 'OSS',
    'Pakistan': 'PAK',
    'Panama': 'PAN',
    'Peru': 'PER',
    'Philippines': 'PHL',
    'Palau': 'PLW',
    'Papua New Guinea': 'PNG',
    'Poland': 'POL',
    'Puerto Rico': 'PRI',
    'Korea, Dem. Rep.': 'PRK',
    'Democratic People\'s Republic of Korea': 'PRK',
    'Portugal': 'PRT',
    'Paraguay': 'PRY',
    'Pacific island small states': 'PSS',
    'French Polynesia': 'PYF',
    'Qatar': 'QAT',
    'Romania': 'ROU',
    'Russian Federation': 'RUS',
    'Rwanda': 'RWA',
    'South Asia': 'SAS',
    'Saudi Arabia': 'SAU',
    'The former state union Serbia and Montenegro': 'SCG',
    'Serbia and Montenegro': 'SCG',
    'Sudan': 'SDN',
    'Senegal': 'SEN',
    'Singapore': 'SGP',
    'Solomon Islands': 'SLB',
    'Sierra Leone': 'SLE',
    'El Salvador': 'SLV',
    'San Marino': 'SMR',
    'Somalia': 'SOM',
    'Serbia': 'SRB',
    'Sub-Saharan Africa (developing only)': 'SSA',
    'South Sudan': 'SSD',
    'Sub-Saharan Africa (all income levels)': 'SSF',
    'Small states': 'SST',
    'Sao Tome and Principe': 'STP',
    'Suriname': 'SUR',
    'Slovak Republic': 'SVK',
    'Slovakia': 'SVK',
    'Slovenia': 'SVN',
    'Sweden': 'SWE',
    'Swaziland': 'SWZ',
    'Sint Maarten (Dutch part)': 'SXM',
    'Seychelles': 'SYC',
    'Syrian Arab Republic': 'SYR',
    'Turks and Caicos Islands': 'TCA',
    'Chad': 'TCD',
    'Togo': 'TGO',
    'Thailand': 'THA',
    'Tajikistan': 'TJK',
    'Turkmenistan': 'TKM',
    'Timor-Leste': 'TLS',
    'Tonga': 'TON',
    'Trinidad and Tobago': 'TTO',
    'Tunisia': 'TUN',
    'Turkey': 'TUR',
    'Tuvalu': 'TUV',
    'Tanzania': 'TZA',
    'United Republic of Tanzania': 'TZA',
    'Uganda': 'UGA',
    'Ukraine': 'UKR',
    'Upper middle income': 'UMC',
    'Uruguay': 'URY',
    'United States': 'USA',
    'United States of America': 'USA',
    'Uzbekistan': 'UZB',
    'St. Vincent and the Grenadines': 'VCT',
    'Saint Vincent and the Grenadines': 'VCT',
    'Venezuela, RB': 'VEN',
    'Venezuela (Bolivarian Republic of)': 'VEN',
    'Virgin Islands (U.S.)': 'VIR',
    'Vietnam': 'VNM',
    'Viet Nam': 'VNM',
    'Vanuatu': 'VUT',
    'West Bank and Gaza': 'PSE',
    'World': 'WLD',
    'Samoa': 'WSM',
    'Yemen, Rep.': 'YEM',
    'Yemen': 'YEM',
    'South Africa': 'ZAF',
    'Congo, Dem. Rep.': 'COD',
    'Zambia': 'ZMB',
    'Zimbabwe': 'ZWE'
}

def step1():
    data = []
    my_countries = {}
    with open('attr_data/WDI/WDI_csv/WDI_Data.csv', 'r') as csvfile:
        headers = ['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code', '1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']
        years = ['1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']
        reader = csv.DictReader(csvfile, fieldnames=headers)
        first = True
        for row in reader:
            if first:
                first = False
                continue
            # if row['1960'] != '':
            #     print row['1960']
            # continue
            data_point = {}
            data_point['id'] = row['Country Code']
            # my_countries[data_point['id']]
            data_point['country'] = row['Country Name']
            attr = row['Indicator Code']
            attr_name = row['Indicator Name']
            # sys.stdout.write('Country: ' + data_point['id'] + ' ' + attr_name + '\r')
            for year in years:
                attr_value = row[year]
                if attr_value == '':
                    continue
                sys.stdout.write('Country: ' + data_point['id'] + ' # '+ year + '\r')
                # data_point[attr] = {
                #     'value': attr_value,
                #     'name': attr_name
                # }
                # data_point['date'] = year
                if data_point['id'] in my_countries:
                    if year in my_countries[data_point['id']]:
                        my_countries[data_point['id']][year][attr] = {
                            'value': attr_value,
                            'name': attr_name
                        }
                    else:
                        my_countries[data_point['id']][year] = {
                                attr: {
                                    'value': attr_value,
                                    'name': attr_name
                                }
                        }
                else:
                    my_countries[data_point['id']] = {
                        year: {
                            attr: {
                                'value': attr_value,
                                'name': attr_name
                            }
                        }
                    }
                #
                # if len(data) > 0:
                #     for old_country in data:
                #         if old_country['id'] == data_point['id'] and old_country['date'] == data_point['date']:
                #             # Update data
                #             old_country[attr] = attr_value
                #         else:
                #             # Append new data
                #             data.append(data_point)
                # else:
                #     data.append(data_point)
        for i in my_countries:
            print i
        # print my_countries

        output = open('attr_data/WDI/WDI_csv/data.pkl', 'wb')
        # Pickle dictionary using protocol 0.
        pickle.dump(my_countries, output)

        g = open('attr_data/WDI/WDI_csv/attr.json', 'w')
        g.write(json.dumps(data))
        g.close()
        output.close()


def step2():
    # client = MongoClient('mongodb://192.168.99.100:5999/')
    data = pickle.load(open('attr_data/WDI/WDI_csv/data.pkl'))
    # db = client['topodb']
    # collection = db.WDI
    mongo_data = []
    for country in data:
        for year in data[country]:
            entry = {}
            entry['id'] = country
            try:
                entry['name'] = [i for i in country_code if country_code[i] == country][0]
            except:
                continue
            entry['date'] = year
            entry['attrs'] = {}
            for attr in data[country][year]:
                new_attr = attr.replace('.', '-')
                sys.stdout.write('Country: ' + entry['id'] + ' # '+ attr + '\r')
                entry['attrs'][new_attr] = data[country][year][attr]
            mongo_data.append(entry)
            # Push to mongodb!
            # collection.insert_one(entry)

    g = open('attr_data/WDI/WDI_csv/WDIJSON.json', 'w')
    g.write(json.dumps(mongo_data))
    g.close()

    # output = open('attr_data/WDI/WDI_csv/WDImongodata.pkl', 'wb')
    # # Pickle dictionary using protocol 0.
    # pickle.dump(mongo_data, output)
    #
    # g = open('attr_data/WDI/WDI_csv/WDIattr.json', 'w')
    # g.write(json.dumps(data))
    # g.close()
    # output.close()
    # for point in mongo_data:
    #     print point
    #     break

step2()
