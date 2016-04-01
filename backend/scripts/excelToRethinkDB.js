'use strict';

var r = require('rethinkdb');
var config = require(__dirname + '/../config.js');

var connection= null;
console.log(config.rethinkdb.host, config.rethinkdb.port);
r.connect(config.rethinkdb, function(err, conn) {
    if (err) throw err;
    connection = conn;
    var db = r.db(config.rethinkdb.db);

    /* Load excel.xlsx */
    var data = require(config.data);

    /* Create Countries DB */
    db.tableCreate('countries').run(connection, function(err, result) {
        if (err) throw err;
        console.log(JSON.stringify(result, null, 2));
        /* Populate Countries DB */
        db.table('countries').insert(data.objects.countries).run(connection, function(err, result) {
            if (err) throw err;
            console.log(JSON.stringify(result, null, 2));
        });
    });

    /* Create Regions DB */
    db.tableCreate('regions').run(connection, function(err, result) {
        if (err) throw err;
        console.log(JSON.stringify(result, null, 2));

        /* Populate Regions DB */
        db.table('regions').insert(data.objects.provinces).run(connection, function(err, result) {
            if (err) throw err;
            console.log(JSON.stringify(result, null, 2));
        });
    });


});
