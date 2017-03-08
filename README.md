> Epidemiological Database container:
* mongoexpress for database explorer
* Jupyter Notebook for analysis
* MongoDB for Database
* NodeJS for extra backend features


## Install

To start all containers run the following command:

```sh
$ docker-compose -f docker-compose-prod.yml up -d
```

## Usage

To access the database viewer go to the following URL:

https://compare.cbs.dtu.dk:10080/dashboard/

(If running on another server the URL should be updated accordingly: https://URL:10080/dashboard/)

The user and password can be found in the docker-compose-prod.yml file (not part of the repository for security reasons) in the mongoexpress section:

* ME_CONFIG_BASICAUTH_USERNAME: ""
* ME_CONFIG_BASICAUTH_PASSWORD: ""

By default SSL is enabled and the container expects the certificates to be located here:

/etc/ssl/private/servercerts/

For testing SSL can be turned off bit commenting the following environment variables in the docker-compose-prod.yml file:

```yml
mongoexpress:
    image: mongo-express:latest
    ports:
        - "10080:8081"
    links:
        - mongo
    environment:
        ME_CONFIG_MONGODB_SERVER: mongo
        ME_CONFIG_MONGODB_PORT: 27017
        #ME_CONFIG_BASICAUTH_USERNAME: ""
        #ME_CONFIG_BASICAUTH_PASSWORD: ""
        ME_CONFIG_SITE_BASEURL: "/dashboard/"
        #ME_CONFIG_SITE_SSL_ENABLED: "true"
        #ME_CONFIG_SITE_SSL_CRT_PATH: ""
        #ME_CONFIG_SITE_SSL_KEY_PATH: ""
```

To access the Jupyter Notebook go to the following URL:

http://compare.cbs.dtu.dk:4434/tree

## Data import

Import data to MongoDB database:
```sh
# Import file in CSV format with header indicating field names
$ docker exec epidatabase_mongo_1 mongoimport --host 0.0.0.0:27017 -j 16 -d epidb -c "DATASET_NAME" --file /data/FILE_NAME --type csv --batchSize=100 --headerline

# Import file in TSV format with header indicating field names
$ docker exec epidatabase_mongo_1 mongoimport --host 0.0.0.0:27017 -j 16 -d epidb -c "DATASET_NAME" --file /data/FILE_NAME --type tsv --batchSize=100 --headerline
```

More information on MongoImport can be found [here](https://docs.mongodb.com/manual/reference/program/mongoimport/)


## License

MIT © [Jose Luis Bellod Cisneros](https://github.com/josl)


[npm-image]: https://badge.fury.io/js/topodb.svg
[npm-url]: https://npmjs.org/package/topodb
[travis-image]: https://travis-ci.org/josl/topodb.svg?branch=master
[travis-url]: https://travis-ci.org/josl/topodb
[daviddm-image]: https://david-dm.org/josl/topodb.svg?theme=shields.io
[daviddm-url]: https://david-dm.org/josl/topodb
