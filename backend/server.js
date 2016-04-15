var express = require('express');
var MongoClient = require('mongodb')
    .MongoClient;
var url = 'mongodb://mongo:27017/topodb';
// var url = 'mongodb://192.168.99.100:5999/topodb';
var assert = require('assert');

// var bodyParser = require('body-parser');
var app = express();
var Console = require('console');

var findDocuments = function (country, db, callback) {
    // Get the documents collection
    var collection = db.collection('WDI');
    // Find some documents
    var query = {};
    if (country !== 'all') {
        query.name = country;
    }
    collection.find(query)
        .toArray(function (err, docs) {
            assert.equal(err, null);
            console.log("Found these following records");
            console.dir(docs.length);
            callback(docs);
        });
};

// app.use(function (req, res, next) {
//     res.header('Access-Control-Allow-Origin', '*');
//     res.header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS');
//     res.header('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content-Type, Accept');
//     next();
// });

// middleware function to start serving the files directly
app.use('/map', express.static(__dirname + '/frontend/map'));

app.use('/time_series', express.static(__dirname + '/frontend/time_series'));

app.use('/stats', express.static(__dirname + '/frontend/stats'));

app.get('/', function (req, res) {
    res.send('Hellos World!');
});

app.get('/test', function (req, res) {
    res.send('Hello MY World!');
});

app.get('/api/:country', function (req, res) {
    console.log(req.params.country);
    var country = req.params.country;
    MongoClient.connect(url, function (err, db) {
        assert.equal(null, err);
        console.log("Connected correctly to server");
        findDocuments(country, db, function (docs) {
            console.log(docs[0]);
            res.send(docs);
            db.close();
        });
    });
});

var server = app.listen(80, function () {
    var host = server.address()
        .address;
    var port = server.address()
        .port;

    Console.log('Example app listening at http://%s:%s', host, port);
});
