// var mongoose = require('mongoose');
var attr_data = require('../../attr_data/WDI/pink/attr.json');
// var attr_data = require('/usr/data/WDI/attr.json');
var MongoClient = require('mongodb').MongoClient;
var assert = require('assert');
var url = 'mongodb://192.168.99.100:5999/topodb';

var insertDocuments = function(db, callback) {
      // Get the documents collection
      var collection = db.collection('metadata');
      // Insert some documents
      collection.insertMany(attr_data, function(err, result) {
          console.log(err, result);
          console.log("Inserted all documents into the document collection");
          callback(result);
      });
};

MongoClient.connect(url, function(err, db) {
      assert.equal(null, err);
      console.log("Connected correctly to server");

      insertDocuments(db, function() {
          db.close();
      });

});
// mongoose.connect('mongodb://192.168.99.100:5999/topodb', {
// // mongoose.connect('mongodb://mongo/topodb', {
//     server: { socketOptions: {keepAlive: 120}},
//     replset: { socketOptions: {keepAlive: 120}}
// });
//
// var Schema = mongoose.Schema;
//
// var attrSchema = new Schema({
//       id:  String,
//       name: String,
//       // attr_code: { value: String, name: Date }, // Added later
//       date: Date,
// });
//
// var db = mongoose.connection;
// db.on('error', console.error.bind(console, 'connection error:'));
// db.once('open', function() {
//     // we're connected!
//     attr_data.forEach(function(country){
//         attrSchema.add({
//             attr_code: { value: String, name: Date }
//         });
//     });
// });
