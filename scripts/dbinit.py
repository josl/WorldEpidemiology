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
import  urllib2

country_code = {
    'aruba': 'ABW',
    'andorra': 'AND',
    'afghanistan': 'AFG',
    'angola': 'AGO',
    'anguilla': 'AIA',
    'albania': 'ALB',
    'arab world': 'ARB',
    'united arab emirates': 'ARE',
    'argentina': 'ARG',
    'armenia': 'ARM',
    'american samoa': 'ASM',
    'antigua and barbuda': 'ATG',
    'australia': 'AUS',
    'austria': 'AUT',
    'azerbaijan': 'AZE',
    'burundi': 'BDI',
    'belgium': 'BEL',
    'benin': 'BEN',
    'burkina faso': 'BFA',
    'bangladesh': 'BGD',
    'bulgaria': 'BGR',
    'bahrain': 'BHR',
    'bahamas, the': 'BHS',
    'bahamas': 'BHS',
    'bosnia and herzegovina': 'BIH',
    'belarus': 'BLR',
    'belize': 'BLZ',
    'bermuda': 'BMU',
    'bolivia': 'BOL',
    'bolivia (plurinational state of)': 'BOL',
    'brazil': 'BRA',
    'barbados': 'BRB',
    'brunei darussalam': 'BRN',
    'british indian ocean territory': 'IOT',
    'bhutan': 'BTN',
    'botswana': 'BWA',
    'central african republic': 'CAF',
    'canada': 'CAN',
    'central europe and the baltics': 'CEB',
    'switzerland': 'CHE',
    'channel islands': 'CHI',
    'chile': 'CHL',
    'china': 'CHN',
    'china (exc. hong kong & macao)': 'CHN',
    'china, mainland': 'CHN',
    'cote d\'ivoire': 'CIV',
    u'c\u2122te d\'ivoire': 'CIV',
    'c\xc3\xb4te d\'ivoire': 'CIV',
    'cameroon': 'CMR',
    'cocos (keeling) islands': 'CCK',
    'congo, rep.': 'COG',
    'congo': 'COG',
    'democratic republic of the congo': 'COG',
    'cook islands': 'COK',
    'colombia': 'COL',
    'comoros': 'COM',
    'cabo verde': 'CPV',
    'cape verde': 'CPV',
    'costa rica': 'CRI',
    'caribbean small states': 'CSS',
    'cuba': 'CUB',
    'curacao': 'CUW',
    'cura\xe7ao': 'CUW',
    'netherlands antilles, curacao': 'CUW',
    'christmas island': 'CXR',
    'cayman islands': 'CYM',
    'cyprus': 'CYP',
    'czech republic': 'CZE',
    'czechoslovakia': 'CSK',
    'germany': 'DEU',
    'germany fr': 'DEU',
    'germany,  federal republic of': 'DEU',
    'djibouti': 'DJI',
    'dominica': 'DMA',
    'denmark': 'DNK',
    'dominican republic': 'DOM',
    'algeria': 'DZA',
    'east asia & pacific (developing only)': 'EAP',
    'east asia & pacific (all income levels)': 'EAS',
    'europe & central asia (developing only)': 'ECA',
    'europe & central asia (all income levels)': 'ECS',
    'ecuador': 'ECU',
    'egypt, arab rep.': 'EGY',
    'egypt': 'EGY',
    'euro area': 'EMU',
    'eritrea': 'ERI',
    'spain': 'ESP',
    'estonia': 'EST',
    'ethiopia': 'ETH',
    'ethiopia pdr': 'ETH',
    'european union': 'EUU',
    'fragile and conflict affected situations': 'FCS',
    'finland': 'FIN',
    'fiji': 'FJI',
    'falkland islands (malvinas)': 'FLK',
    'france': 'FRA',
    'faeroe islands': 'FRO',
    'faroe islands': 'FRO',
    'micronesia, fed. sts.': 'FSM',
    'micronesia (federated states of)': 'FSM',
    'gabon': 'GAB',
    'united kingdom': 'GBR',
    'united kingdom of great britain and northern ireland': 'GBR',
    'georgia': 'GEO',
    'ghana': 'GHA',
    'gibraltar': 'GIB',
    'guinea': 'GIN',
    'guadeloupe': 'GLP',
    'gambia, the': 'GMB',
    'gambia': 'GMB',
    'guinea-bissau': 'GNB',
    'equatorial guinea': 'GNQ',
    'greece': 'GRC',
    'grenada': 'GRD',
    'greenland': 'GRL',
    'guatemala': 'GTM',
    'french guiana': 'GUF',
    'guam': 'GUM',
    'guyana': 'GUY',
    'high income': 'HIC',
    'hong kong sar, china': 'HKG',
    'china, hong kong sar': 'HKG',
    'honduras': 'HND',
    'heavily indebted poor countries (hipc)': 'HPC',
    'croatia': 'HRV',
    'haiti': 'HTI',
    'hungary': 'HUN',
    'indonesia': 'IDN',
    'isle of man': 'IMN',
    'india': 'IND',
    'not classified': 'INX',
    'ireland': 'IRL',
    'iran, islamic rep.': 'IRN',
    'iran (islamic republic of)': 'IRN',
    'iran': 'IRN',
    'iraq': 'IRQ',
    'iceland': 'ISL',
    'israel': 'ISR',
    'italy': 'ITA',
    'jamaica': 'JAM',
    'jersey': 'JEY',
    'jordan': 'JOR',
    'japan': 'JPN',
    'kazakhstan': 'KAZ',
    'kenya': 'KEN',
    'kyrgyz republic': 'KGZ',
    'kyrgyzstan': 'KGZ',
    'cambodia': 'KHM',
    'kiribati': 'KIR',
    'st. kitts and nevis': 'KNA',
    'saint kitts and nevis': 'KNA',
    'korea, rep.': 'KOR',
    'republic of korea': 'KOR',
    'kosovo': 'KSV',
    'kuwait': 'KWT',
    'latin america & caribbean (developing only)': 'LAC',
    'lao pdr': 'LAO',
    'lao people\'s democratic republic': 'LAO',
    'lebanon': 'LBN',
    'liberia': 'LBR',
    'libya': 'LBY',
    'st. lucia': 'LCA',
    'saint lucia': 'LCA',
    'latin america & caribbean (all income levels)': 'LCN',
    'least developed countries: un classification': 'LDC',
    'low income': 'LIC',
    'liechtenstein': 'LIE',
    'sri lanka': 'LKA',
    'lower middle income': 'LMC',
    'low & middle income': 'LMY',
    'lesotho': 'LSO',
    'lithuania': 'LTU',
    'luxembourg': 'LUX',
    'latvia': 'LVA',
    'macao sar, china': 'MAC',
    'china, macao sar': 'MAC',
    'st. martin (french part)': 'MAF',
    'morocco': 'MAR',
    'monaco': 'MCO',
    'moldova': 'MDA',
    'republic of moldova': 'MDA',
    'madagascar': 'MDG',
    'maldives': 'MDV',
    'middle east & north africa (all income levels)': 'MEA',
    'mexico': 'MEX',
    'marshall islands': 'MHL',
    'middle income': 'MIC',
    'macedonia, fyr': 'MKD',
    'the former yugoslav republic of macedonia': 'MKD',
    'mali': 'MLI',
    'malta': 'MLT',
    'myanmar': 'MMR',
    'middle east & north africa (developing only)': 'MNA',
    'montenegro': 'MNE',
    'mongolia': 'MNG',
    'northern mariana islands': 'MNP',
    'mozambique': 'MOZ',
    'mauritania': 'MRT',
    'mauritius': 'MUS',
    'malawi': 'MWI',
    'malaysia': 'MYS',
    'north america': 'NAC',
    'namibia': 'NAM',
    'new caledonia': 'NCL',
    'niger': 'NER',
    'nigeria': 'NGA',
    'nicaragua': 'NIC',
    'niue': 'NIU',
    'netherlands': 'NLD',
    'high income: nonoecd': 'NOC',
    'norfolk island': 'NFK',
    'norway': 'NOR',
    'nepal': 'NPL',
    'nauru': 'NRU',
    'new zealand': 'NZL',
    'high income: oecd': 'OEC',
    'oecd members': 'OED',
    'oman': 'OMN',
    'other small states': 'OSS',
    'pakistan': 'PAK',
    'panama': 'PAN',
    'pitcairn islands': 'PCN',
    'peru': 'PER',
    'philippines': 'PHL',
    'palau': 'PLW',
    'papua new guinea': 'PNG',
    'poland': 'POL',
    'puerto rico': 'PRI',
    'korea, dem. rep.': 'PRK',
    'democratic people\'s republic of korea': 'PRK',
    'portugal': 'PRT',
    'paraguay': 'PRY',
    'pacific island small states': 'PSS',
    'french polynesia': 'PYF',
    'qatar': 'QAT',
    'romania': 'ROU',
    'russian federation': 'RUS',
    'rwanda': 'RWA',
    'south asia': 'SAS',
    'saudi arabia': 'SAU',
    'saudi arabia, middle income group': 'SAU',
    'saudi arabia, all cities': 'SAU',
    'the former state union serbia and montenegro': 'SCG',
    'serbia and montenegro': 'SCG',
    'sudan': 'SDN',
    'senegal': 'SEN',
    'singapore': 'SGP',
    'solomon islands': 'SLB',
    'sierra leone': 'SLE',
    'el salvador': 'SLV',
    'san marino': 'SMR',
    'somalia': 'SOM',
    'serbia': 'SRB',
    'sub-saharan africa (developing only)': 'SSA',
    'south sudan': 'SSD',
    'sub-saharan africa (all income levels)': 'SSF',
    'small states': 'SST',
    'sao tome and principe': 'STP',
    'suriname': 'SUR',
    'slovak republic': 'SVK',
    'slovakia': 'SVK',
    'slovenia': 'SVN',
    'sweden': 'SWE',
    'swaziland': 'SWZ',
    'sint maarten (dutch part)': 'SXM',
    'sint maarten (dutch part)': 'SXM',
    'seychelles': 'SYC',
    'svalbard and jan mayen islands': 'SJM',
    'svalbard and jan mayen': 'SJM',
    'syrian arab republic': 'SYR',
    'ussr': 'SUN',
    'turks and caicos islands': 'TCA',
    'chad': 'TCD',
    'togo': 'TGO',
    'thailand': 'THA',
    'tajikistan': 'TJK',
    'tokelau': 'TKL',
    'turkmenistan': 'TKM',
    'timor-leste': 'TLS',
    'tonga': 'TON',
    'trinidad and tobago': 'TTO',
    'tunisia': 'TUN',
    'turkey': 'TUR',
    'tuvalu': 'TUV',
    'china, taiwan province of': 'TWN',
    'tanzania': 'TZA',
    'united republic of tanzania': 'TZA',
    'uganda': 'UGA',
    'ukraine': 'UKR',
    'upper middle income': 'UMC',
    'uruguay': 'URY',
    'united states': 'USA',
    'united states of america': 'USA',
    'uzbekistan': 'UZB',
    'st. vincent and the grenadines': 'VCT',
    'saint vincent and the grenadines': 'VCT',
    'venezuela, rb': 'VEN',
    'venezuela (bolivarian republic of)': 'VEN',
    'virgin islands (u.s.)': 'VIR',
    'united states virgin islands': 'VIR',
    'vietnam': 'VNM',
    'viet nam': 'VNM',
    'vanuatu': 'VUT',
    'west bank and gaza': 'PSE',
    'occupied palestinian territory': 'PSE',
    'palestine, state of': 'PSE',
    'gaza strip (palestine)': 'PSE',
    'world': 'WLD',
    'samoa': 'WSM',
    'yemen, rep.': 'YEM',
    'yemen ar rp': 'YEM',
    'yemen': 'YEM',
    'yemen dem': 'YEM',
    'south africa': 'ZAF',
    'congo, dem. rep.': 'COD',
    'zambia': 'ZMB',
    'zambia, low income group': 'ZMB',
    'zimbabwe': 'ZWE',
    'holy see': 'VAT',
    'martinique': 'MTQ',
    'mayotte': 'MYT',
    'montserrat': 'MSR',
    'netherlands antilles (former)': 'ANT',
    'netherlands antilles': 'ANT',
    u'r\u017dunion': 'REU',
    'r\xe9union': 'REU',
    'r\xc3\xa9union': 'REU',
    'saint helena, ascension and tristan da cunha': 'TAA',
    'saint pierre and miquelon': 'SPM',
    'sudan (former)': 'SDN',
    'the former yugoslav republic of macedonia': 'MKD',
    'british virgin islands': 'VIR',
    'wallis and futuna islands': 'WLF',
    'yugoslav sfr': 'YUG',
    'west bank and gaza strip': 'PSE',
    'wake island': 'WAK',
    'western sahara': 'ESH'
}

cities = [

]

regions = [
    'solomon islands, honiara',
    'central african republic, bangui',
    'guinea, conakry',
    'falkland islands (malvinas), stanley',
    'guinea, conakry',
    'chile, santiago',
    'saint kitts and nevis, saint kitts',
    'south sudan, funafuti',
    'namibia, windhoek',
    'cook islands, rarotonga',
    'nicaragua, managua',
    'india, urban non-manual employees',
    'sri lanka, colombo',
    'kiribati, tarawa',
    'cambodia, phnom penh',
    'marshall islands, majuro',
    'rwanda, kigali',
    'togo, lome',
    'saint-martin (french part)',
    'congo, brazzaville',
    'guinea-bissau, bissau',
    'united republic of tanzania, zanzibar',
    'panama, panama',
    'india, industrial workers',
    'niger, niamey',
    'myanmar, yangon',
    'uruguay, montevideo',
    'madagascar, antananarivo',
    'mali, bamako',
    'argentina, buenos aires',
    'sierra leone, freetown',
    "c\xc3\xb4te d'ivoire, abidjan",
    "chad, n'djamena",
    'venezuela (bolivarian republic of), caracas',
    'new caledonia, noumea',
    'kenya, nairobi',
    'india, agricultural workers',
    'northern mariana islands, saipan',
    'madagascar, antananarivo, europ.',
    'mozambique, maputo',
    'gambia, banjul',
    'maldives, male',
    'mongolia, ulan bator',
    'senegal, dakar',
    'saint vincent and the grenadines, saint vincent',
    'india, delhi, industrial workers',
    'paraguay, asuncion',
    'angola, luanda',
    'malaysia, sabah',
    'ethiopia, addis abeba',
    'lebanon, beyrouth',
    'syrian arab republic, damas',
    'cape verde, praia',
    'suriname, paramaribo',
    'united republic of tanzania, tanganyika',
    'oman, muscat',
    'gabon, libreville',
    'swaziland, mbabane-manzini',
    'equatorial guinea, malabo',
    'guyana, georgetown',
    'benin, cotonou',
    'brazil, sao paulo',
    'burkina faso, ouagadougou',
    'bahamas, new providence',
    'burundi, bujumbura',
    'peru, lima'
]

excluded_countries = [
    u'country',
    u'developing countries',
    u'africa',
    u'eastern africa',
    u'middle africa',
    u'southern africa',
    u'western africa',
    u'north africa (exc sudan)',
    u'sub-saharan africa',
    u'asia',
    u'caucasus and central asia',
    u'east asia',
    u'east asia (exc china)',
    u'southern asia',
    u'south asia (exc india)',
    u'south-eastern asia',
    u'west asia',
    u'central america',
    u'south america',
    u'latin america and the caribbean',
    u'caribbean',
    u'latin america',
    u'oceania',
    u'developed countries'
    u'least developed countries',
    u'land locked developing countries',
    u'small island developing states',
    u'low income economies',
    u'lower-middle-income economies',
    u'low income food deficit countries',
    u'developed countries',
    u'least developed countries',
    'low income economies',
    'south-eastern asia',
    'developing countries',
    'eastern africa',
    'northern africa',
    'middle africa + (total)',
    'small island developing states',
    'sub-saharan africa',
    'oceania + (total)',
    'eastern europe + (total)',
    'annex i countries',
    'polynesia + (total)',
    'western asia',
    'melanesia',
    'latin america',
    'western africa + (total)',
    'americas + (total)',
    'eu(27)ex.int',
    'micronesia + (total)',
    'southern asia + (total)',
    'least developed countries',
    'least developed countries + (total)',
    'north africa (exc sudan)',
    'european union (exc intra-trade)',
    'central america + (total)',
    'caribbean + (total)',
    'western europe + (total)',
    'northern america',
    'land locked developing countries + (total)',
    'landlocked developing countries + (total)',
    'southern asia',
    'asia + (total)',
    'east asia',
    'french southern and antarctic territories',
    'northern europe',
    'land locked developing countries',
    'net food importing developing countries + (total)',
    'asia',
    'western africa',
    'caucasus and central asia',
    'central asia + (total)',
    'central asia',
    'africa + (total)',
    'europe',
    'eu(25)ex.int',
    'world + (total)',
    'antarctic region',
    'small island developing states + (total)',
    'low income food deficit countries + (total)',
    'eastern asia + (total)',
    'latin america and the caribbean',
    'south asia (exc india)',
    'south-eastern asia + (total)',
    'polynesia',
    'non-annex i countries',
    'eu(15)ex.int',
    'developed countries',
    'melanesia + (total)',
    'northern america + (total)',
    'west asia',
    'western asia + (total)',
    'africa',
    'eastern europe',
    'southern africa + (total)',
    'european union + (total)',
    'middle africa',
    'micronesia',
    'antarctica',
    'eastern asia',
    'germany nl',
    'southern europe + (total)',
    'australia and new zealand + (total)',
    'southern africa',
    'northern africa + (total)',
    'lower-middle-income economies',
    'northern europe + (total)',
    'low income food deficit countries',
    'americas',
    'south america + (total)',
    'eu(12)ex.int',
    'central america',
    'pacific islands trust territory',
    'eastern africa + (total)',
    'net food importing developing countries',
    'oecd',
    'europe + (total)',
    'western europe',
    'east asia (exc china)',
    'australia & new zealand',
    'south america',
    'oceania',
    'caribbean',
    'southern europe',
    'belgium-luxembourg',
    'australia & new zealand + (total)',
]

path = 'attr_data/FAO/'

processes_files = [
    'ASTI_Research_Spending_E_All_Data_(Norm).csv',
    'ASTI_Researchers_E_All_Data_(Norm).csv',
    'CommodityBalances_Crops_E_All_Data_(Norm).csv',
    'CommodityBalances_LivestockFish_E_All_Data_(Norm).csv',
    'ConsumerPriceIndices_E_All_Data_(Norm).csv',
    'Deflators_E_All_Data_(Norm).csv',
    'Emissions_Agriculture_Agriculture_total_E_All_Data_(Norm).csv',
    'Emissions_Agriculture_Burning_Savanna_E_All_Data_(Norm).csv',
    'Emissions_Agriculture_Burning_crop_residues_E_All_Data_(Norm).csv',
    'Emissions_Agriculture_Crop_Residues_E_All_Data_(Norm).csv',
    'Emissions_Agriculture_Cultivated_Organic_Soils_E_All_Data_(Norm).csv',
    'Emissions_Agriculture_Energy_E_All_Data_(Norm).csv',
    'Emissions_Agriculture_Enteric_Fermentation_E_All_Data_(Norm).csv',
    'Emissions_Agriculture_Manure_Management_E_All_Data_(Norm).csv',
    'Emissions_Agriculture_Manure_applied_to_soils_E_All_Data_(Norm).csv',
    'Emissions_Agriculture_Manure_left_on_pasture_E_All_Data_(Norm).csv',
    'Emissions_Agriculture_Rice_Cultivation_E_All_Data_(Norm).csv',
    'Emissions_Agriculture_Synthetic_Fertilizers_E_All_Data_(Norm).csv',
    'Emissions_Land_Use_Burning_Biomass_E_All_Data_(Norm).csv',
    'Emissions_Land_Use_Cropland_E_All_Data_(Norm).csv',
    'Emissions_Land_Use_Forest_Land_E_All_Data_(Norm).csv',
    'Emissions_Land_Use_Grassland_E_All_Data_(Norm).csv',
    'Emissions_Land_Use_Land_Use_Total_E_All_Data_(Norm).csv',
    'Employment_Indicators_E_All_Data_(Norm).csv',
    'Environment_AirClimateChange_E_All_Data.csv',
    'Environment_Energy_E_All_Data.csv',
    'Environment_Fertilizers_E_All_Data.csv',
    'Environment_Land_E_All_Data.csv',
    'Environment_Livestock_E_All_Data.csv',
    'Environment_Pesticides_E_All_Data.csv',
    'Environment_Soil_E_All_Data.csv',
    'Environment_Water_E_All_Data.csv',
    'Food_Security_Data_E_All_Data_(Norm).csv'
]

headers_old = {
    'FoodBalanceSheets_E_All_Data_(Norm).csv': ["Country Code", "Country", "Item Code", "Item", "Element Code", "Element", "Year Code", "Year", "Unit", "Value", "Flag"],
    'FoodSupply_Crops_E_All_Data_(Norm).csv': ["Country Code", "Country", "Item Code", "Item", "Element Code", "Element", "Year Code", "Year", "Unit", "Value", "Flag"],
    'FoodSupply_LivestockFish_E_All_Data_(Norm).csv': ["Country Code", "Country", "Item Code", "Item", "Element Code", "Element", "Year Code", "Year", "Unit", "Value", "Flag"],
    # 'Food_Aid_Shipments_WFP_E_All_Data_(Norm).csv': ["Recipient Country Code", "Recipient Country", "Item Code", "Item", "Donor Country Code", "Donor Country", "Year Code", "Year", "Unit", "Value", "Flag"],
    # 'Food_Security_Data_E_All_Data_(Norm).csv': ["Country Code", "Country", "Item Code", "Item", "Element Code", "Element", "Year Code", "Year", "Unit", "Value", "Flag"],
    'Forestry_E_All_Data_(Norm).csv': ["Country Code", "Country", "Item Code", "Item", "Element Code", "Element", "Year Code", "Year", "Unit", "Value", "Flag"],
    # 'Forestry_Trade_Flows_E_All_Data_(Norm).csv': ["Reporter Country Code", "Reporter Countries", "Partner Country Code", "Partner Countries", "Item Code", "Item", "Element Code", "Element", "Year Code", "Year", "Unit", "Value", "Flag"],
    'Inputs_FertilizersTradeValues_E_All_Data_(Norm).csv': ["Country Code", "Country", "Item Code", "Item", "Element Code", "Element", "Year Code", "Year", "Unit", "Value", "Flag"],
    'Inputs_Fertilizers_E_All_Data_(Norm).csv': ["Country Code", "Country", "Item Code", "Item", "Element Code", "Element", "Year Code", "Year", "Unit", "Value", "Flag"],
    'Inputs_Land_E_All_Data_(Norm).csv': ["Country Code", "Country", "Item Code", "Item", "Element Code", "Element", "Year Code", "Year", "Unit", "Value", "Flag"],
    'Inputs_Pesticides_Trade_E_All_Data_(Norm).csv': ["Country Code", "Country", "Item Code", "Item", "Element Code", "Element", "Year Code", "Year", "Unit", "Value", "Flag"],
    'Inputs_Pesticides_Use_E_All_Data_(Norm).csv': ["Country Code", "Country", "Item Code", "Item", "Element Code", "Element", "Year Code", "Year", "Unit", "Value", "Flag"],
    'Investment_CapitalStock_E_All_Data.csv': ["CountryCode", "Country", "ItemCode", "Item", "ElementGroup", "ElementCode", "Element", "Year", "Unit", "Value", "Flag"],
    'Investment_CreditAgriculture_E_All_Data_(Norm).csv': ["Country Code", "Country", "Item Code", "Item", "Element Code", "Element", "Year Code", "Year", "Unit", "Value", "Flag"],
    'Investment_GovernmentExpenditure_E_All_Data_(Norm).csv': ["Country Code", "Country", "Item Code", "Item", "Element Code", "Element", "Year Code", "Year", "Unit", "Value", "Flag"],
    'Investment_MachineryArchive_E_All_Data.csv': ["CountryCode", "Country", "ItemCode", "Item", "ElementGroup", "ElementCode", "Element", "Year", "Unit", "Value", "Flag"],
    'Investment_Machinery_E_All_Data.csv': ["CountryCode", "Country", "ItemCode", "Item", "ElementGroup", "ElementCode", "Element", "Year", "Unit", "Value", "Flag"],
    'Macro-Statistics_Key_Indicators_E_All_Data_(Norm).csv': ["Country Code", "Country", "Item Code", "Item", "Element Code", "Element", "Year Code", "Year", "Unit", "Value", "Flag"],
    'Population_E_All_Data_(Norm).csv': ["Country Code", "Country", "Item Code", "Item", "Element Code", "Element", "Year Code", "Year", "Unit", "Value", "Flag"],
    'Price_Indices_E_All_Data_(Norm).csv': ["Country Code", "Country", "Item Code", "Item", "Element Code", "Element", "Year Code", "Year", "Unit", "Value", "Flag"],
    'PricesArchive_E_All_Data.csv': ["CountryCode", "Country", "ItemCode", "Item", "ElementGroup", "ElementCode", "Element", "Year", "Unit", "Value", "Flag"],
    'Prices_E_All_Data_(Norm).csv': ["Country Code", "Country", "Item Code", "Item", "Element Code", "Element", "Year Code", "Year", "Unit", "Value", "Flag"],
    'Prices_Monthly_E_All_Data_(Norm).csv': ["Country Code", "Country", "Item Code", "Item", "Months Code", "Months", "Year Code", "Year", "Unit", "Value", "Flag"],
    'Production_CropsProcessed_E_All_Data_(Norm).csv': ["Country Code", "Country", "Item Code", "Item", "Element Code", "Element", "Year Code", "Year", "Unit", "Value", "Flag"],
    'Production_Crops_E_All_Data_(Norm).csv': ["Country Code", "Country", "Item Code", "Item", "Element Code", "Element", "Year Code", "Year", "Unit", "Value", "Flag"],
    'Production_Indices_E_All_Data_(Norm).csv': ["Country Code", "Country", "Item Code", "Item", "Element Code", "Element", "Year Code", "Year", "Unit", "Value", "Flag"],
    'Production_LivestockPrimary_E_All_Data_(Norm).csv': ["Country Code", "Country", "Item Code", "Item", "Element Code", "Element", "Year Code", "Year", "Unit", "Value", "Flag"],
    'Production_LivestockProcessed_E_All_Data_(Norm).csv': ["Country Code", "Country", "Item Code", "Item", "Element Code", "Element", "Year Code", "Year", "Unit", "Value", "Flag"],
    'Production_Livestock_E_All_Data_(Norm).csv': ["Country Code", "Country", "Item Code", "Item", "Element Code", "Element", "Year Code", "Year", "Unit", "Value", "Flag"],
    'Resources_FertilizersArchive_E_All_Data.csv': ["CountryCode", "Country", "ItemCode", "Item", "ElementGroup", "ElementCode", "Element", "Year", "Unit", "Value", "Flag"],
    'Trade_Crops_Livestock_E_All_Data_(Norm).csv': ["Country Code", "Country", "Item Code", "Item", "Element Code", "Element", "Year Code", "Year", "Unit", "Value", "Flag"],
    # 'Trade_DetailedTradeMatrix_E_All_Data_(Norm).csv': ["Reporter Country Code", "Reporter Countries", "Partner Country Code", "Partner Countries", "Item Code", "Item", "Element Code", "Element", "Year Code", "Year", "Unit", "Value", "Flag"],
    'Trade_Indices_E_All_Data_(Norm).csv': ["Country Code", "Country", "Item Code", "Item", "Element Code", "Element", "Year Code", "Year", "Unit", "Value", "Flag"],
    'Trade_LiveAnimals_E_All_Data_(Norm).csv': ["Country Code", "Country", "Item Code", "Item", "Element Code", "Element", "Year Code", "Year", "Unit", "Value", "Flag"],
    'Value_of_Production_E_All_Data_(Norm).csv': ["Country Code", "Country", "Item Code", "Item", "Element Code", "Element", "Year Code", "Year", "Unit", "Value", "Flag"]
}

headers = {
    'ASTI_Research_Spending_E_All_Data_(Norm).csv': ["Country Code", "Country", "Item Code", "Item", "Element Code", "Element", "Year Code", "Year", "Unit", "Value", "Flag"],
    'ASTI_Researchers_E_All_Data_(Norm).csv': ["Country Code", "Country", "Item Code", "Item", "Element Code", "Element", "Year Code", "Year", "Unit", "Value", "Flag"],
    'CommodityBalances_Crops_E_All_Data_(Norm).csv': ["Country Code", "Country", "Item Code", "Item", "Element Code", "Element", "Year Code", "Year", "Unit", "Value", "Flag"],
    'CommodityBalances_LivestockFish_E_All_Data_(Norm).csv': ["Country Code", "Country", "Item Code", "Item", "Element Code", "Element", "Year Code", "Year", "Unit", "Value", "Flag"],
    'ConsumerPriceIndices_E_All_Data_(Norm).csv': ["Country Code", "Country", "Item Code", "Item", "Months Code", "Months", "Year Code", "Year", "Unit", "Value", "Flag", "Note"],
    'Deflators_E_All_Data_(Norm).csv': ["Country Code", "Country", "Item Code", "Item", "Element Code", "Element", "Year Code", "Year", "Unit", "Value", "Flag"],
    'Emissions_Agriculture_Agriculture_total_E_All_Data_(Norm).csv': ["Country Code", "Country", "Item Code", "Item", "Element Code", "Element", "Year Code", "Year", "Unit", "Value", "Flag"],
    'Emissions_Agriculture_Burning_Savanna_E_All_Data_(Norm).csv': ["Country Code", "Country", "Item Code", "Item", "Element Code", "Element", "Year Code", "Year", "Unit", "Value", "Flag"],
    'Emissions_Agriculture_Burning_crop_residues_E_All_Data_(Norm).csv': ["Country Code", "Country", "Item Code", "Item", "Element Code", "Element", "Year Code", "Year", "Unit", "Value", "Flag"],
    'Emissions_Agriculture_Crop_Residues_E_All_Data_(Norm).csv': ["Country Code", "Country", "Item Code", "Item", "Element Code", "Element", "Year Code", "Year", "Unit", "Value", "Flag"],
    'Emissions_Agriculture_Cultivated_Organic_Soils_E_All_Data_(Norm).csv': ["Country Code", "Country", "Item Code", "Item", "Element Code", "Element", "Year Code", "Year", "Unit", "Value", "Flag"],
    'Emissions_Agriculture_Energy_E_All_Data_(Norm).csv': ["Country Code", "Country", "Item Code", "Item", "Element Code", "Element", "Year Code", "Year", "Unit", "Value", "Flag"],
    'Emissions_Agriculture_Enteric_Fermentation_E_All_Data_(Norm).csv': ["Country Code", "Country", "Item Code", "Item", "Element Code", "Element", "Year Code", "Year", "Unit", "Value", "Flag"],
    'Emissions_Agriculture_Manure_Management_E_All_Data_(Norm).csv': ["Country Code", "Country", "Item Code", "Item", "Element Code", "Element", "Year Code", "Year", "Unit", "Value", "Flag"],
    'Emissions_Agriculture_Manure_applied_to_soils_E_All_Data_(Norm).csv': ["Country Code", "Country", "Item Code", "Item", "Element Code", "Element", "Year Code", "Year", "Unit", "Value", "Flag"],
    'Emissions_Agriculture_Manure_left_on_pasture_E_All_Data_(Norm).csv': ["Country Code", "Country", "Item Code", "Item", "Element Code", "Element", "Year Code", "Year", "Unit", "Value", "Flag"],
    'Emissions_Agriculture_Rice_Cultivation_E_All_Data_(Norm).csv': ["Country Code", "Country", "Item Code", "Item", "Element Code", "Element", "Year Code", "Year", "Unit", "Value", "Flag"],
    'Emissions_Agriculture_Synthetic_Fertilizers_E_All_Data_(Norm).csv': ["Country Code", "Country", "Item Code", "Item", "Element Code", "Element", "Year Code", "Year", "Unit", "Value", "Flag"],
    'Emissions_Land_Use_Burning_Biomass_E_All_Data_(Norm).csv': ["Country Code", "Country", "Item Code", "Item", "Element Code", "Element", "Year Code", "Year", "Unit", "Value", "Flag"],
    'Emissions_Land_Use_Cropland_E_All_Data_(Norm).csv': ["Country Code", "Country", "Item Code", "Item", "Element Code", "Element", "Year Code", "Year", "Unit", "Value", "Flag"],
    'Emissions_Land_Use_Forest_Land_E_All_Data_(Norm).csv': ["Country Code", "Country", "Item Code", "Item", "Element Code", "Element", "Year Code", "Year", "Unit", "Value", "Flag"],
    'Emissions_Land_Use_Grassland_E_All_Data_(Norm).csv': ["Country Code", "Country", "Item Code", "Item", "Element Code", "Element", "Year Code", "Year", "Unit", "Value", "Flag"],
    'Emissions_Land_Use_Land_Use_Total_E_All_Data_(Norm).csv': ["Country Code", "Country", "Item Code", "Item", "Element Code", "Element", "Year Code", "Year", "Unit", "Value", "Flag"],
    'Employment_Indicators_E_All_Data_(Norm).csv': ["Country Code", "Country", "Source Code", "Source", "Indicator Code", "Indicator", "Year Code", "Year", "Unit", "Value", "Flag"],
    'Environment_AirClimateChange_E_All_Data.csv': ["CountryCode", "Country", "ItemCode", "Item", "ElementGroup", "ElementCode", "Element", "Year", "Unit", "Value", "Flag"],
    'Environment_Energy_E_All_Data.csv': ["CountryCode", "Country", "ItemCode", "Item", "ElementGroup", "ElementCode", "Element", "Year", "Unit", "Value", "Flag"],
    'Environment_Fertilizers_E_All_Data.csv': ["CountryCode", "Country", "ItemCode", "Item", "ElementGroup", "ElementCode", "Element", "Year", "Unit", "Value", "Flag"],
    'Environment_Land_E_All_Data.csv': ["CountryCode", "Country", "ItemCode", "Item", "ElementGroup", "ElementCode", "Element", "Year", "Unit", "Value", "Flag"],
    'Environment_Livestock_E_All_Data.csv': ["CountryCode", "Country", "ItemCode", "Item", "ElementGroup", "ElementCode", "Element", "Year", "Unit", "Value", "Flag"],
    'Environment_Pesticides_E_All_Data.csv': ["CountryCode", "Country", "ItemCode", "Item", "ElementGroup", "ElementCode", "Element", "Year", "Unit", "Value", "Flag"],
    'Environment_Soil_E_All_Data.csv': ["CountryCode", "Country", "ItemCode", "Item", "ElementGroup", "ElementCode", "Element", "Year", "Unit", "Value", "Flag"],
    'Environment_Water_E_All_Data.csv': ["CountryCode", "Country", "ItemCode", "Item", "ElementGroup", "ElementCode", "Element", "Year", "Unit", "Value", "Flag"],
    'FoodBalanceSheets_E_All_Data_(Norm).csv': ["Country Code", "Country", "Item Code", "Item", "Element Code", "Element", "Year Code", "Year", "Unit", "Value", "Flag"],
    'FoodSupply_Crops_E_All_Data_(Norm).csv': ["Country Code", "Country", "Item Code", "Item", "Element Code", "Element", "Year Code", "Year", "Unit", "Value", "Flag"],
    'FoodSupply_LivestockFish_E_All_Data_(Norm).csv': ["Country Code", "Country", "Item Code", "Item", "Element Code", "Element", "Year Code", "Year", "Unit", "Value", "Flag"],
    # 'Food_Aid_Shipments_WFP_E_All_Data_(Norm).csv': ["Recipient Country Code", "Recipient Country", "Item Code", "Item", "Donor Country Code", "Donor Country", "Year Code", "Year", "Unit", "Value", "Flag"],
    'Food_Security_Data_E_All_Data_(Norm).csv': ["Country Code", "Country", "Item Code", "Item", "Element Code", "Element", "Year Code", "Year", "Unit", "Value", "Flag"],
    'Forestry_E_All_Data_(Norm).csv': ["Country Code", "Country", "Item Code", "Item", "Element Code", "Element", "Year Code", "Year", "Unit", "Value", "Flag"],
    # 'Forestry_Trade_Flows_E_All_Data_(Norm).csv': ["Reporter Country Code", "Reporter Countries", "Partner Country Code", "Partner Countries", "Item Code", "Item", "Element Code", "Element", "Year Code", "Year", "Unit", "Value", "Flag"],
    'Inputs_FertilizersTradeValues_E_All_Data_(Norm).csv': ["Country Code", "Country", "Item Code", "Item", "Element Code", "Element", "Year Code", "Year", "Unit", "Value", "Flag"],
    'Inputs_Fertilizers_E_All_Data_(Norm).csv': ["Country Code", "Country", "Item Code", "Item", "Element Code", "Element", "Year Code", "Year", "Unit", "Value", "Flag"],
    'Inputs_Land_E_All_Data_(Norm).csv': ["Country Code", "Country", "Item Code", "Item", "Element Code", "Element", "Year Code", "Year", "Unit", "Value", "Flag"],
    'Inputs_Pesticides_Trade_E_All_Data_(Norm).csv': ["Country Code", "Country", "Item Code", "Item", "Element Code", "Element", "Year Code", "Year", "Unit", "Value", "Flag"],
    'Inputs_Pesticides_Use_E_All_Data_(Norm).csv': ["Country Code", "Country", "Item Code", "Item", "Element Code", "Element", "Year Code", "Year", "Unit", "Value", "Flag"],
    'Investment_CapitalStock_E_All_Data.csv': ["CountryCode", "Country", "ItemCode", "Item", "ElementGroup", "ElementCode", "Element", "Year", "Unit", "Value", "Flag"],
    'Investment_CreditAgriculture_E_All_Data_(Norm).csv': ["Country Code", "Country", "Item Code", "Item", "Element Code", "Element", "Year Code", "Year", "Unit", "Value", "Flag"],
    'Investment_GovernmentExpenditure_E_All_Data_(Norm).csv': ["Country Code", "Country", "Item Code", "Item", "Element Code", "Element", "Year Code", "Year", "Unit", "Value", "Flag"],
    'Investment_MachineryArchive_E_All_Data.csv': ["CountryCode", "Country", "ItemCode", "Item", "ElementGroup", "ElementCode", "Element", "Year", "Unit", "Value", "Flag"],
    'Investment_Machinery_E_All_Data.csv': ["CountryCode", "Country", "ItemCode", "Item", "ElementGroup", "ElementCode", "Element", "Year", "Unit", "Value", "Flag"],
    'Macro-Statistics_Key_Indicators_E_All_Data_(Norm).csv': ["Country Code", "Country", "Item Code", "Item", "Element Code", "Element", "Year Code", "Year", "Unit", "Value", "Flag"],
    'Population_E_All_Data_(Norm).csv': ["Country Code", "Country", "Item Code", "Item", "Element Code", "Element", "Year Code", "Year", "Unit", "Value", "Flag"],
    'Price_Indices_E_All_Data_(Norm).csv': ["Country Code", "Country", "Item Code", "Item", "Element Code", "Element", "Year Code", "Year", "Unit", "Value", "Flag"],
    'PricesArchive_E_All_Data.csv': ["CountryCode", "Country", "ItemCode", "Item", "ElementGroup", "ElementCode", "Element", "Year", "Unit", "Value", "Flag"],
    'Prices_E_All_Data_(Norm).csv': ["Country Code", "Country", "Item Code", "Item", "Element Code", "Element", "Year Code", "Year", "Unit", "Value", "Flag"],
    'Prices_Monthly_E_All_Data_(Norm).csv': ["Country Code", "Country", "Item Code", "Item", "Months Code", "Months", "Year Code", "Year", "Unit", "Value", "Flag"],
    'Production_CropsProcessed_E_All_Data_(Norm).csv': ["Country Code", "Country", "Item Code", "Item", "Element Code", "Element", "Year Code", "Year", "Unit", "Value", "Flag"],
    'Production_Crops_E_All_Data_(Norm).csv': ["Country Code", "Country", "Item Code", "Item", "Element Code", "Element", "Year Code", "Year", "Unit", "Value", "Flag"],
    'Production_Indices_E_All_Data_(Norm).csv': ["Country Code", "Country", "Item Code", "Item", "Element Code", "Element", "Year Code", "Year", "Unit", "Value", "Flag"],
    'Production_LivestockPrimary_E_All_Data_(Norm).csv': ["Country Code", "Country", "Item Code", "Item", "Element Code", "Element", "Year Code", "Year", "Unit", "Value", "Flag"],
    'Production_LivestockProcessed_E_All_Data_(Norm).csv': ["Country Code", "Country", "Item Code", "Item", "Element Code", "Element", "Year Code", "Year", "Unit", "Value", "Flag"],
    'Production_Livestock_E_All_Data_(Norm).csv': ["Country Code", "Country", "Item Code", "Item", "Element Code", "Element", "Year Code", "Year", "Unit", "Value", "Flag"],
    'Resources_FertilizersArchive_E_All_Data.csv': ["CountryCode", "Country", "ItemCode", "Item", "ElementGroup", "ElementCode", "Element", "Year", "Unit", "Value", "Flag"],
    'Trade_Crops_Livestock_E_All_Data_(Norm).csv': ["Country Code", "Country", "Item Code", "Item", "Element Code", "Element", "Year Code", "Year", "Unit", "Value", "Flag"],
    # 'Trade_DetailedTradeMatrix_E_All_Data_(Norm).csv': ["Reporter Country Code", "Reporter Countries", "Partner Country Code", "Partner Countries", "Item Code", "Item", "Element Code", "Element", "Year Code", "Year", "Unit", "Value", "Flag"],
    'Trade_Indices_E_All_Data_(Norm).csv': ["Country Code", "Country", "Item Code", "Item", "Element Code", "Element", "Year Code", "Year", "Unit", "Value", "Flag"],
    'Trade_LiveAnimals_E_All_Data_(Norm).csv': ["Country Code", "Country", "Item Code", "Item", "Element Code", "Element", "Year Code", "Year", "Unit", "Value", "Flag"],
    'Value_of_Production_E_All_Data_(Norm).csv': ["Country Code", "Country", "Item Code", "Item", "Element Code", "Element", "Year Code", "Year", "Unit", "Value", "Flag"]
}

def FAO_init():
    client = MongoClient('mongodb://localhost:5999/')
    db = client['topodb']
    collection = db.FAO_countries
    collection_domains = db.FAO_domains
    collection_elements = db.FAO_elements
    mongo_data = []
    attributes = {}
    elements = Set()
    fao_domains = []
    print "Let\'s start with FAO!"
    for filename in os.listdir(path):
        print filename
        if filename.split('.')[1] != 'csv':
            continue
        with open(path + filename) as f:
            # if f in processes_files:
            #     continue
            try:
                reader = csv.DictReader(f, fieldnames=headers[filename])
            except:
                continue
            first = True
            fao_domains.append({'Domain': filename.split('.')[0]})
            for row in reader:
                entry = {}
                if first or row[headers[filename][1]].lower().decode('latin-1').encode('utf-8') in excluded_countries or row[headers[filename][1]].lower().decode('latin-1').encode('utf-8') in regions:
                    first = False
                    continue
                # sys.stdout.write('Country: ' + country_code[row[headers[filename][1]].lower().decode('latin-1').encode('utf-8')] + '\r')
                sys.stdout.write('Country: ' + row[headers[filename][1]].lower().decode('latin-1').encode('utf-8') + '\r')
                date_index = headers[filename].index('Year')
                entry = row
                for attr in entry:
                    entry[attr] = entry[attr].decode('latin-1').encode('utf-8')
                country_index = headers[filename].index('Country')
                entry['Domain'] = filename.split('.')[0]
                try:
                    entry['Country ID'] = country_code[row[headers[filename][country_index]].lower()]
                except:
                    print row[headers[filename][country_index]].lower()
                    entry['Country ID'] = row[headers[filename][country_index]].lower
                    entry['country-code'] = 'REPLACE'
                if '-' in row[headers[filename][7]]:
                    dates = range(int(row[headers[filename][date_index]].split(
                        '-')[0]), int(row[headers[filename][date_index]].split('-')[1]))
                    for year in dates:
                        entry['Date'] = year
                        try:
                            entry['Country'] = entry['Country']
                        except:
                            print entry['Country']
                        try:
                            collection.insert_one(entry)
                        except:
                            continue
                else:
                    entry['Date'] = row[headers[filename][date_index]]
                    try:
                        entry['Country'] = entry['Country']
                    except:
                        print entry['Country']
                    try:
                        collection.insert_one(entry)
                    except:
                        continue

    collection_domains.insert_many(fao_domains)


def WDI_init():
    data = []
    client = MongoClient('mongodb://localhost:5999/')
    db = client['topodb']
    collection = db.WDI_countries
    collection_indicators = db.WDI_indicators
    indicators = {}
    print "Let\'s start with WDI!"
    with open('attr_data/WDI/Indicators.csv', 'r') as csvfile:
        print "File read"
        reader = csv.DictReader(csvfile)
        print "CSV parsed"
        first = True
        for row in reader:
            if first:
                first = False
                continue
            data_point = {}
            data_point['country-id'] = row['CountryCode']
            data_point['country-name'] = row['CountryName']
            data_point['attr-name'] = row['IndicatorName']
            data_point['attr'] = row['IndicatorCode']
            data_point['year'] = row['Year']
            data_point['value'] = row['Value']
            indicators[row['IndicatorCode']] = row['IndicatorName']
            sys.stdout.write('Country: ' + row['CountryCode'] + '\tAttr: ' + row['IndicatorName'] +'\r')

            collection.insert_one(data_point)
        collection_indicators.insert_many([{'code': k, 'name': v} for k, v in indicators.items()])

def parse_flight_data_point(data):
    # From city / To city / Year / Nb.air carriers / Passenger revenue traffic / Freight revenue traffic (tonnes) / Mail revenue traffic (tonnes)
    # [u 'AALBORG (DENMARK)', u 'COPENHAGEN (DENMARK)', 2002, u 'Q4', 1, 56159, 8.4, 0.6]

    answer = []
    for data_point in data:
        try:
            country_in = country_code[data_point[0].split('(')[1].strip().replace(')', '').lower()]
        except:
            country_in = data_point[0].split('(')[1].strip().replace(')', '').lower()
        try:
            country_out = country_code[data_point[1].split('(')[1].strip().replace(')', '').lower()]
        except:
            country_out = data_point[1].split('(')[1].strip().replace(')', '').lower()
        sys.stdout.write('Country I: ' + country_in + '\Country O: ' + country_out + '\r')
        answer.append({
            'city-origin': data_point[0].split('(')[0].strip().lower(),
            'city-destiny': data_point[1].split('(')[0].strip().lower(),
            'year': data_point[2],
            'nb-air-carriers': data_point[4],
            'quarter': data_point[3],
            'passenger-revenue-traffic': data_point[5],
            'freight-revenue-traffic_tonnes': data_point[6],
            'mail-revenue-traffic_tonnes': data_point[7],
            'country-origin': country_in,
            'country-destiny': country_out
        })
    return answer

def flight_init():
    data = []
    client = MongoClient('mongodb://localhost:5999/')
    db = client['topodb']
    collection = db.flight_data
    print "Let\'s start with flight data!"
    url = 'http://dataplusapi.icao.int/dataplus/formB/basic?year%5B%5D=2016&year%5B%5D=2015&year%5B%5D=2014&year%5B%5D=2013&year%5B%5D=2012&year%5B%5D=2011&year%5B%5D=2010&year%5B%5D=2009&year%5B%5D=2008&year%5B%5D=2007&year%5B%5D=2006&year%5B%5D=2005&year%5B%5D=2004&year%5B%5D=2003&year%5B%5D=2002&year%5B%5D=2001&year%5B%5D=2000&year%5B%5D=1999&year%5B%5D=1998&year%5B%5D=1997&year%5B%5D=1996&year%5B%5D=1995&year%5B%5D=1994&year%5B%5D=1993&year%5B%5D=1992&year%5B%5D=1991&year%5B%5D=1990&year%5B%5D=1989&year%5B%5D=1988&year%5B%5D=1987&year%5B%5D=1986&year%5B%5D=1985&year%5B%5D=1984&year%5B%5D=1983&year%5B%5D=1982&airCarrierId%5B%5D=120336&airCarrierId%5B%5D=120338&airCarrierId%5B%5D=120736&airCarrierId%5B%5D=120519&airCarrierId%5B%5D=15093453&airCarrierId%5B%5D=120442&airCarrierId%5B%5D=120443&airCarrierId%5B%5D=120342&airCarrierId%5B%5D=120201&airCarrierId%5B%5D=19505932&airCarrierId%5B%5D=120347&airCarrierId%5B%5D=8178807&airCarrierId%5B%5D=120444&airCarrierId%5B%5D=120445&airCarrierId%5B%5D=120520&airCarrierId%5B%5D=120446&airCarrierId%5B%5D=120621&airCarrierId%5B%5D=120623&airCarrierId%5B%5D=120521&airCarrierId%5B%5D=120358&airCarrierId%5B%5D=120447&airCarrierId%5B%5D=8714755&airCarrierId%5B%5D=121277&airCarrierId%5B%5D=120449&airCarrierId%5B%5D=120450&airCarrierId%5B%5D=120776&airCarrierId%5B%5D=120263&airCarrierId%5B%5D=121317&airCarrierId%5B%5D=120626&airCarrierId%5B%5D=121324&airCarrierStateId%5B%5D=10614&airCarrierStateId%5B%5D=10637&airCarrierStateId%5B%5D=10763&airCarrierStateId%5B%5D=10643&airCarrierStateId%5B%5D=10603&airCarrierStateId%5B%5D=10663&airCarrierStateId%5B%5D=10621&airCarrierStateId%5B%5D=10696&filterNames%5B%5D=year&filterNames%5B%5D=airCarrierId&filterNames%5B%5D=airCarrierStateId&dimension%5B%5D=from+City&dimension%5B%5D=to+City&dimension%5B%5D=year&dimension%5B%5D=quarter&quarter%5B%5D=Q1&quarter%5B%5D=Q2&quarter%5B%5D=Q3&quarter%5B%5D=Q4&_search=false&nd=1462201101438&rows=20&sidx=from+City&sord=asc'
    req = urllib2.Request(url + '&page=1')
    response = urllib2.urlopen(req)
    json_data = response.read()
    json_obj = json.loads(json_data)
    print "Flight json ready!!"
    # {u'totalPages': 11442, u'totalRecords': 228835, u'page': 1, u'rowsPerPage': 20}
    pages = json_obj['pagination']['totalPages']
    print pages
    data_parsed = parse_flight_data_point(json_obj['data'])
    collection.insert_many(data_parsed)
    for page in range(1, pages+1):
        print page
        req = urllib2.Request(url + '&page=' + str(page))
        response = urllib2.urlopen(req)
        json_data = response.read()
        json_obj = json.loads(json_data)
        data_parsed = parse_flight_data_point(json_obj['data'])
        collection.insert_many(data_parsed)

def ecdc_init():
    data = []
    client = MongoClient('mongodb://localhost:5999/')
    db = client['topodb']
    collection = db.ECDC
    indicators = {}
    print "Let\'s start with ECDC!"
    with open('attr_data/ECDC/antibacterial_and_antiviral_use_2014_ECDC.json', 'r') as jsonfile:
        print "File read"
        json_data = json.load(jsonfile)
        print "JSON parsed"
        for entry in json_data:
            try:
                entry['country-code'] = country_code[entry['Country'].lower()]
            except:
                entry['country-code'] = 'REPLACE'
            entry_point = {}
            for (key, value) in entry.items():
                entry_point[key.replace('.', ' ')] = value
            collection.insert_one(entry_point)

def who_init():

    file_mapping = {
        'Age-stand_mort_rate_by_cause_(per100000pop)_WHO.json': {
            'desc': 'Age-standardized death rate by three major cause groups, both sexes (Data by country)',
            'url': 'http://apps.who.int/gho/data/view.main.GHEASDRCTRYMAJOR',
            'id': 'GHEASDRCTRYMAJOR'
        },
        'Households_using_an_improved_drinking-water_source_____WHO.json': {
            'desc': 'Improved drinking-water source (Data by country)',
            'url': 'http://apps.who.int/gho/data/node.imr.EQ_WATERIMPROVED?lang=en',
            'id': 4437
        },
        'Number_of_reported_cases_of_cholera_WHO.json': {
            'desc': 'Number of reported cases of cholera (Infectious diseases)',
            'url': 'http://apps.who.int/gho/data/node.imr.CHOLERA_0000000001?lang=en',
            'id': 3168
        },
        'density_of_hospitals_WHO.json': {
            'desc': 'Total density per 100 000 population: Hospitals (Health systems)',
            'url': 'http://apps.who.int/gho/data/node.imr.DEVICES00?lang=en',
            'id': 3361
        }
    }
    data = []
    client = MongoClient('mongodb://localhost:5999/')
    db = client['topodb']
    collection = db.WHO
    collection_indicators = db.WHO_indicators
    non_indicators = ['ID', 'Country', 'Year']
    path = 'attr_data/WHO/'
    collection_data = []
    print "Let\'s start with WHO!"
    for filename in os.listdir(path):
        indicators = set()
        # with open('attr_data/ECDC/' + filename) as f:
        with open(path + filename) as f:
            json_data = json.load(f)
            print "JSON parsed"
            file_indicators = set()
            for entry in json_data:
                entry_point = {}
                for (key, value) in entry.items():
                    if key not in non_indicators:
                        indicators.add(key)
                        # attrs = file_mapping[filename]
                        # attrs['attr'] = key
                        # indicators.append(attrs)
                    entry_point[key.replace('.', ' ')] = value
                try:
                    entry_point['country-code'] = country_code[entry_point['Country'].lower()]
                except:
                    entry_point['country-code'] = 'REPLACE'
                # collection.insert_one(entry_point)
            temp = file_mapping[filename]
            for indicator in list(indicators):
                new_entry = {}
                for attr in temp:
                    new_entry[attr] = temp[attr]
                new_entry['attr'] = indicator
                print new_entry
                collection_data.append(new_entry)
    import pprint
    pprint.pprint(collection_data)
    collection_indicators.insert_many(collection_data)
                # collection_indicators.insert_one(temp)
            # print indicators_collection
            # collection_indicators.insert_many(indicators_collection)
            # collection_indicators.insert_many(
            #     [file_mapping[filename].update({'attr': indicator}) for indicator in list(indicators)]
            # )

print "Hello EpiDb fans!"

# ecdc_init()
# flight_init()
# WDI_init()
# FAO_init()
who_init()


# ecdc_init()
# flight_init()
# WDI_init()
# FAO_init()
# who_init()
