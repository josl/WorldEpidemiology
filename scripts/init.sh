####################################
#
# $1 = container_name or container ID
#
####################################

# Topology in TopoJSON format
docker exec $1 mongoimport --host 0.0.0.0:27017 -j 16 -d topodb -c topology --file /usr/data/topoDB.json--batchSize=100
# Countries in GeoJSON format
docker exec $1 mongoimport --host 0.0.0.0:27017 -j 16 -d topodb -c countries --file /usr/data/countries_features.json --jsonArray --batchSize=100
# Provinces in GeoJSON format
docker exec $1 mongoimport --host 0.0.0.0:27017 -j 16 -d topodb -c provinces --file /usr/data/provinces_features.json --jsonArray --batchSize=100
