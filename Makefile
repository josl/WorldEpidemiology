GENERATED_FILES = geo_data/topoDB.json
JSONUnits=geo_data/subunits.json geo_data/units.json geo_data/sovereignty.json geo_data/population.json
JSONCountries=geo_data/countries.json

WHERE_IBERIA = -where "ADM0_A3 IN ('ESP', 'PRT')"

# WHERE = $(WHERE_IBERIA)
WHERE = -where "gn_id != -99"

PROPERTIES_CO1 = pop=Population,longname=FORMAL_EN,name=NAME,area=Area,
PROPERTIES_CO2= continent=CONTINENT,subregion=SUBREGION,id=ISO3,capital=Capital

PROPERTIES_PROV1= name=gn_name,longname=woe_label,country=admin,id=geonameid,
PROPERTIES_PROV2= pop=population,adm0=adm0_a3,date=mod_date

COUNTRY_PROP= geo_data/countries_pop.tsv
PROV_PROP_A= geo_data/provinces_A.tsv
PROV_PROP_B= geo_data/provinces_B1.tsv
PROV_PROP_C= geo_data/provinces_C1.tsv
PROV_PROP_D= geo_data/provinces_D1.tsv

COUNTRYID= ISO3,ISO_A3,adm0_a3
PROVINCEID= gn_id,geonameid

TOPOJSON= node --max_old_space_size=10240 `which topojson`

TOPOFILES=geo_data/countries_topo.json geo_data/provinces_topo_A.json geo_data/provinces_topo_B.json geo_data/provinces_topo_C.json geo_data/provinces_topo_D.json

ALLPROVINCES=prov1=geo_data/provinces_topo_A.json prov4=geo_data/provinces_topo_B.json prov3=geo_data/provinces_topo_C.json prov2=geo_data/provinces_topo_D.json

all: $(GENERATED_FILES)

geo_data/topoDB.json: geo_data/countries_topo.json geo_data/provinces_topo_A.json geo_data/provinces_topo_B.json geo_data/provinces_topo_C.json geo_data/provinces_topo_D.json
	$(TOPOJSON) --quantization 1e5 --stitch-poles false --shapefile-encoding utf8 -o geo_data/topoDB.json -p -- countries=geo_data/countries_topo.json provinces=geo_data/provinces.json
	cp geo_data/topoDB.json backend/frontend/map.

geo_data/countries_topo.json: $(COUNTRY_PROP) $(JSONCountries)
	$(TOPOJSON) --stitch-poles false --shapefile-encoding utf8 -o geo_data/countries_topo.json -e $(COUNTRY_PROP) -p $(PROPERTIES_CO1)$(PROPERTIES_CO2) --id-property=$(COUNTRYID) -- $(JSONCountries)

headers:
	echo "geonameid	name	population	mod_date" | \
	cat - geo_data/provinces_B.tsv > geo_data/provinces_B1.tsv
	echo "geonameid	name	population	mod_date" | \
	cat - geo_data/provinces_C.tsv > geo_data/provinces_C1.tsv
	echo "geonameid	name	population	mod_date" | \
	cat - geo_data/provinces_D.tsv > geo_data/provinces_D1.tsv

geo_data/provinces_topo.json: geo_data/provinces.json
	$(TOPOJSON) --stitch-poles false -o geo_data/provinces_topo.json -p $(PROPERTIES_PROV1)$(PROPERTIES_PROV2) --id-property=$(PROVINCEID) -- geo_data/provinces.json

geo_data/allDataProvinces.json:
	$(TOPOJSON) --stitch-poles false -o geo_data/provinces_topo_D.json -e $(PROV_PROP_D) -p $(PROPERTIES_PROV1)$(PROPERTIES_PROV2) --id-property=$(PROVINCEID) -- geo_data/provinces.json
	$(TOPOJSON) --stitch-poles false -o geo_data/provinces_topo_C.json -e $(PROV_PROP_C) -p $(PROPERTIES_PROV1)$(PROPERTIES_PROV2) --id-property=$(PROVINCEID) -- geo_data/provinces.json
	$(TOPOJSON) --stitch-poles false -o geo_data/provinces_topo_B.json -e $(PROV_PROP_B) -p $(PROPERTIES_PROV1)$(PROPERTIES_PROV2) --id-property=$(PROVINCEID) -- geo_data/provinces.json
	$(TOPOJSON) --stitch-poles false -o geo_data/provinces_topo_A.json -e $(PROV_PROP_A) -p $(PROPERTIES_PROV1)$(PROPERTIES_PROV2) --id-property=$(PROVINCEID) -- geo_data/provinces.json

geo_data/ne_10m_admin_0_countries/ne_10m_admin_0_countries.shp:
	curl -o geo_data/countries.zip 'http://www.naturalearthdata.com/http//www.naturalearthdata.com/download/10m/cultural/ne_10m_admin_0_countries.zip'
	unzip geo_data/countries.zip -d data
	touch geo_data/ne_10m_admin_0_countries/ne_10m_admin_0_countries.shp

geo_data/ne_10m_admin_0_map_units/ne_10m_admin_0_map_units.shp:
	curl -o geo_data/units.zip 'http://www.naturalearthdata.com/http//www.naturalearthdata.com/download/10m/cultural/ne_10m_admin_0_map_units.zip'
	unzip geo_data/units.zip -d data
	touch geo_data/ne_10m_admin_0_map_units/ne_10m_admin_0_map_units.shp

geo_data/ne_10m_admin_0_map_subunits/ne_10m_admin_0_map_subunits.shp:
	curl -o geo_data/subunits.zip 'http://www.naturalearthdata.com/http//www.naturalearthdata.com/download/10m/cultural/ne_10m_admin_0_map_subunits.zip'
	unzip geo_data/subunits.zip -d data
	touch geo_data/ne_10m_admin_0_map_subunits/ne_10m_admin_0_map_subunits.shp

geo_data/ne_10m_admin_0_sovereignty/ne_10m_admin_0_sovereignty.shp:
	curl -o geo_data/sovereignty.zip 'http://www.naturalearthdata.com/http//www.naturalearthdata.com/download/10m/cultural/ne_10m_admin_0_sovereignty.zip'
	unzip geo_data/sovereignty.zip -d data
	touch geo_data/ne_10m_admin_0_sovereignty/ne_10m_admin_0_sovereignty.shp

geo_data/ne_10m_admin_1_states_provinces/ne_10m_admin_1_states_provinces.shp:
	curl -o geo_data/provinces.zip 'http://www.naturalearthdata.com/http//www.naturalearthdata.com/download/10m/cultural/ne_10m_admin_1_states_provinces.zip'
	unzip geo_data/provinces.zip -d data
	touch geo_data/ne_10m_admin_1_states_provinces/ne_10m_admin_1_states_provinces.shp

geo_data/ne_10m_populated_places/ne_10m_populated_places.shp:
	curl -o geo_data/population.zip 'http://www.naturalearthdata.com/http//www.naturalearthdata.com/download/10m/cultural/ne_10m_populated_places.zip'
	unzip geo_data/population.zip
	touch geo_data/ne_10m_populated_places/ne_10m_populated_places.shp

geo_data/countries.json:
	ogr2ogr -f GeoJSON $(WHERE) geo_data/countries.json geo_data/ne_10m_admin_0_countries/ne_10m_admin_0_countries.shp

geo_data/subunits.json:
	ogr2ogr -f GeoJSON $(WHERE) geo_data/subunits.json geo_data/ne_10m_admin_0_map_subunits/ne_10m_admin_0_map_subunits.shp

geo_data/units.json:
	ogr2ogr -f GeoJSON $(WHERE) geo_data/units.json geo_data/ne_10m_admin_0_map_units/ne_10m_admin_0_map_units.shp

geo_data/sovereignty.json:
	ogr2ogr -f GeoJSON $(WHERE) geo_data/sovereignty.json geo_data/ne_10m_admin_0_sovereignty/ne_10m_admin_0_sovereignty.shp

geo_data/provinces.json:
	ogr2ogr -f GeoJSON $(WHERE) geo_data/provinces.json geo_data/ne_10m_admin_1_states_provinces/ne_10m_admin_1_states_provinces.shp

geo_data/population.json:
	ogr2ogr -f GeoJSON $(WHERE) geo_data/population.json geo_data/ne_10m_populated_places/ne_10m_populated_places.shp

geo_data/allCountries.txt:
	curl -o geo_data/allcountries.zip http://download.geonames.org/export/dump/allCountries.zip
	unzip geo_data/allCountries.zip -d data
	touch geo_data/allCountries.txt

	# "geonameid":        # integer id of record in geonames database
	# "name":             # name of geographical point (utf8)
	# "asciiname":        # name of geographical point in  ascii
	# "alternatenames":   # alternatenames
	# "latitude":         # latitude in decimal degrees (wgs84)
	# "longitude":        # longitude in decimal degrees (wgs84)
	# "feature_class":    # http:#www.geonames.org/export/codes.html
	# "feature_code":     # http:#www.geonames.org/export/codes.html
	# "country_code":     # ISO-3166 2-letter country code, 2 char
	# "cc2":              # alternate country codes(ISO-3166)
	# "admin1":           # fipscode
	# "admin2":           # the second administrative division
	# "admin3":           # third level administrative division
	# "admin4":           # fourth level administrative division
	# "population":       # bigint (8 byte int)
	# "elevation":        # in meters, integer
	# "dem":              # digital elevation model
	# "timezone":         # the timezone id
	# "mod_date":         # date of last modification (yyyy-MM-dd)

$(PROV_PROP): geo_data/allCountries.txt
	echo "geonameid	name	asciiname	alternatenames	latitude	longitude	"\
	"feature_class	feature_code	country_code	cc2	admin1	admin2	admin3	"\
	"admin4	population	elevation	dem	timezone	mod_date" | \
	cat - geo_data/allCountries.txt | cut -f 1,2,15,19 > $(PROV_PROP)
	# split -b 100000k $(PROV_PROP) $(PROV_PROP)_part
	# mv  $(PROV_PROP)_part*  $(PROV_PROP)_part*.tsv

	# echo "geonameid	name	population	mod_date" | cat - geo_data/countryInfo.txt
	# 54248345
	# 1-13562086
	# 13562087-27124173
	# 27124174-40686259
	# 40686260-54248345
geo_data/countries.txt:
	curl -o geo_data/countryInfo.txt http://download.geonames.org/export/dump/countryInfo.txt

$(COUNTRY_PROP): geo_data/countries.txt
	curl -o geo_data/countryInfo.txt http://download.geonames.org/export/dump/countryInfo.txt
	echo "ISO	ISO3	ISO-Numeric	fips	Country	Capital	Area	Population	"\
	"Continent	tld	CurrencyCode	CurrencyName	Phone	Postal Code Format	"\
	"Postal Code Regex	Languages	geonameid	neighbours	EquivalentFipsCode" | \
	cat - geo_data/countryInfo.txt  > $(COUNTRY_PROP)

install:
	# Installing node packages
	npm install
	# Installing RethinkDB database
	brew install rethinkdb

db:
	rethinkdb &
	node db/bulkRethinkDB.js

# FIXME fix make rule
web: web/topoDB.json
	cp geo_data/topoDB.json web/.
	grunt

clean:
	rm geo_data/*.json
	rm geo_data/*.tsv
	# rm geo_data/*.zip
	rm rm geo_data/*.txt
	rm rm geo_data/*.tsv
