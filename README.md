#  [![NPM version][npm-image]][npm-url] [![Build Status][travis-image]][travis-url] [![Dependency Status][daviddm-image]][daviddm-url]

> Creation of geographical TopoJSON database based on shapefiles from Natural Earth


## Install

```sh
# Starts both NodeJS and MongoDB servers
$ docker-compose up -d
```


## Usage

Import data to mongodb
```sh
# Topology in TopoJSON format
$ docker exec <CONTAINER_NAME> mongoimport --host 0.0.0.0:27017 -j 16 -d topodb -c topology --file /data/topoDB.json --jsonArray --batchSize=100
# Countries in GeoJSON format
$ docker exec <CONTAINER_NAME> mongoimport --host 0.0.0.0:27017 -j 16 -d topodb -c countries --file /data/countries.json --jsonArray --batchSize=100
# Provinces in GeoJSON format
$ docker exec <CONTAINER_NAME> mongoimport --host 0.0.0.0:27017 -j 16 -d topodb -c provinces --file /data/provinces.json --jsonArray --batchSize=100

```
## License

MIT © [Jose Luis Bellod Cisneros](https://github.com/josl)


[npm-image]: https://badge.fury.io/js/topodb.svg
[npm-url]: https://npmjs.org/package/topodb
[travis-image]: https://travis-ci.org/josl/topodb.svg?branch=master
[travis-url]: https://travis-ci.org/josl/topodb
[daviddm-image]: https://david-dm.org/josl/topodb.svg?theme=shields.io
[daviddm-url]: https://david-dm.org/josl/topodb
