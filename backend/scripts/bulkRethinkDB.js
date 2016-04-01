'use strict';

var r = require('rethinkdb');
var config = require(__dirname + '/../config.js');
var _ = require('lodash');

var connection= null;
console.log(config.rethinkdb.host, config.rethinkdb.port);
r.connect(config.rethinkdb, function(err, conn) {
    if (err) {throw err;}
    connection = conn;
    var db = r.db(config.rethinkdb.db);

    /* Load TopoDB.json */
    var data = require(config.data);
    var countries = require('../data/countries.json');
    var regions = require('../data/provinces.json');

    // Topology Collection
    // db.tableCreate('topology').run(connection, function(err, result) {
    //     if (err) {throw err;}
    //     console.log('topology created', JSON.stringify(result, null, 2));
    //     /* Populate Countries DB */
    //     db.table('topology').insert(data).run(connection, function(err, result) {
    //         if (err) {
    //             console.log('Topology', err);
    //             throw err;
    //         }
    //         console.log('Topology inserted', JSON.stringify(result, null, 2));
    //     });
    // });
    // GeoJSON Collection: countries
    db.tableCreate('countries').run(connection, function(err, result) {
        if (err) {throw err;}
        console.log('countries created', JSON.stringify(result, null, 2));
        /* Populate Countries DB */
        var geoCountries = countries.features;
        for (var i = 0; i < geoCountries.length; i++) {
            db.table('countries').insert({
                id: geoCountries[i].properties.ADM0_A3,
                properties: geoCountries[i].properties,
                location: r.geojson(geoCountries[i].geometry)
            }).run(connection, function(err, result) {
                if (err) {
                    console.log('countries', err);
                    throw err;
                }
                console.log('countries inserted', JSON.stringify(result, null, 2));
            });
        }
    });
    // GeoJSON Collection: provinces
    db.tableCreate('regions').run(connection, function(err, result) {
        if (err) {throw err;}
        console.log('REGIONS created', JSON.stringify(result, null, 2));
        // console.log(data.objects);
        /* Populate Regions DB */
        var geoProvinces = regions.features;
        for (var i = 0; i < geoProvinces.length; i++) {
            var location;
            // http://gis.stackexchange.com/questions/121396/convert-multipolygon-geojson-to-multiple-geojson-polygons
            if (geoProvinces[i].geometry.type === 'MultiPolygon'){
                location = [];
                geoProvinces[i].geometry.coordinates.forEach(function(coords){
                    db.table('regions').insert({
                        id: geoProvinces[i].properties.gn_id,
                        properties: geoProvinces[i].properties,
                        location: r.geojson(geoProvinces[i].geometry)
                    }).run(connection, function(err, result) {
                        if (err) {
                            console.log('regions', err);
                            throw err;
                        }
                        console.log('regions inserted', JSON.stringify(result, null, 2));
                    });
                   var feat={'type':'Polygon','coordinates':coords};

                   }
                );
            }
            else {
                db.table('regions').insert({
                    id: geoProvinces[i].properties.gn_id,
                    properties: geoProvinces[i].properties,
                    location: r.geojson(geoProvinces[i].geometry)
                }).run(connection, function(err, result) {
                    if (err) {
                        console.log('regions', err);
                        throw err;
                    }
                    console.log('regions inserted', JSON.stringify(result, null, 2));
                });
            }
        }
    });
    // /* Create Countries DB */
    // db.tableCreate('countries').run(connection, function(err, result) {
    //     if (err) throw err;
    //     console.log('COUNTRIES created', JSON.stringify(result, null, 2));
    //     /* Populate Countries DB */
    //     db.table('countries').insert(data.objects.countries).run(connection, function(err, result) {
    //         if (err) {
    //             console.log('COUNTRIES', err);
    //             throw err
    //         };
    //         console.log('COUNTRIES inserted', JSON.stringify(result, null, 2));
    //     });
    // });
    //
    // /* Create Regions DB */
    // db.tableCreate('regions').run(connection, function(err, result) {
    //     if (err) throw err;
    //     console.log('REGIONS created', JSON.stringify(result, null, 2));
    //     console.log(data.objects);
    //     /* Populate Regions DB */
    //     db.table('regions').insert(data.objects.provinces).run(connection, function(err, result) {
    //         if (err) {
    //             console.log('REGIONS', err);
    //             throw err
    //         };
    //         console.log('REGIONS inserted', JSON.stringify(result, null, 2));
    //     });
    // });

    /* Countries table */
    // var test = {
    //     id : '', // Country ID: ISO 3166-1 alpha-3. https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3
    //     geometry: {
    //         'coordinates' : [], // TopoJSON array
    //         'type' : ''// GeoJSON Feature: Polygon, Line... etc
    //     },
    //     properties: {
    //         year: {
    //             // Attributes. Complete dataset found in README file
    //         }
    //     },
    //     regions: [{
    //         id : '', // Region ID. GeoNames ADM1 first-order administrative division
    //         geometry: {
    //             'coordinates' : [], // TopoJSON array
    //             'type' : ''// GeoJSON Feature: Polygon, Line... etc
    //         },
    //         properties: {
    //             year: {
    //                 // Attributes. Complete dataset found in README file
    //             }
    //         }
    //     }]
    // };
    // db.tableCreate('countries').run(connection, function(err, result) {
    //     if (err) throw err;
    //     console.log('COUNTRIES created', JSON.stringify(result, null, 2));
    //     /* Populate Countries DB */
    //
    //     // Merge regions into countries based on Country ID (ISO 3166-1 alpha-3)
    //     regions.forEach(function(region){
    //         // region.properties.pop = _.toNumber(region.properties.pop);
    //         var countryID = region.properties.adm0;
    //         var country = _.find(countries, { id: countryID});
    //         country.properties.pop = _.toNumber(country.properties.pop);
    //         if (!country.regions) {
    //             country.regions = [];
    //         }
    //         country.regions.push(region);
    //         country.properties.data =
    //         country.properties = [
    //             country.properties
    //         ]
    //     });
    //     db.table('countries').insert(data.objects.countries).run(connection, function(err, result) {
    //         if (err) {
    //             console.log('COUNTRIES', err);
    //             throw err
    //         };
    //         console.log('COUNTRIES inserted', JSON.stringify(result, null, 2));
    //     });
    // });

});
