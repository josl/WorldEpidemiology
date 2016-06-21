/* jshint undef: true, unused: true */
/* globals d3 */
var width = 1024,
    height = 860;

var projection = d3.geo.mercator()
    .center([0, 0])
    // .rotate(180)
    // .parallels([50, 60])
    // .scale(860)
    .translate([width / 2, height / 2]);

// var projection = d3.geo.mercator()
//     .scale(475)
//     .translate([width / 2, height / 2])
//     .clipAngle(90)
//     .precision(0.1);

var path = d3.geo.path()
    .projection(projection)
    .pointRadius(2);

// normalize the scale to positive numbers
var scale = d3.scale.linear()
    // .domain([lo, hi])
    .range([1, 100]);


var svg = d3.select('body')
        .append('svg')
        .attr('width', width)
        .attr('height', height);

var g = svg.append('g');

svg.append('rect')
    .attr('class', 'overlay')
    .attr('width', width)
    .attr('height', height);

var POPkeys = {};

var carto_countries = d3.cartogram()
    .projection(projection)
    .properties(function(d) {
        return POPkeys[d.id];
    })
    .value(function(d) {
        return scale(d.properties);
    });

function zoomed() {
    g.attr('transform', 'translate(' + d3.event.translate + ')scale(' + d3.event.scale + ')');
}
var zoom = d3.behavior.zoom()
    .scaleExtent([1, 8])
    .on('zoom', zoomed);
svg
    .call(zoom)
    .call(zoom.event);

var color = d3.scale.linear()
            .range(['orange', 'red']);

d3.json('world.json', function(error, data) {
    console.log(data);

    d3.csv("pop.csv", function(error, CSVdata) {
        let rawData = CSVdata;

        let dataById = d3.nest()
          .key(function(d) { return d.NAME; })
          .rollup(function(d) {  return d[0]; })
          .map(data);
          var values = CSVdata
              .map(function(d) {
                  POPkeys[d['NAME']] = d['POPULATION2010'];
                  return +d['POPULATION2010'];
              })
              .filter(function(n) {
                  return !isNaN(n);
              })
              .sort(d3.ascending);
          var minPop = values[0];
          var maxPop = values[values.length - 1];
          console.log(minPop, maxPop);
          scale.domain([minPop, maxPop]);
          color.domain([minPop, maxPop]);

        console.log(data.objects.worldcountries.geometries);
        // Transform Array-like object into array
        data.objects.worldcountries = data.objects.worldcountries.geometries.slice();
        var features = carto_countries(data, data.objects.worldcountries).features;
        g.selectAll("path")
          .data(features)
          .enter()
          .append("path")
            .attr('class', function(d) { return 'country ' + d.id; })
            .attr("fill", function (d) {
                return color(+d.properties);
            })
            .attr("d", carto_countries.path);

    });

});


// g.append("path")
//   .datum(carto_countries.features(data, data.objects.countries.geometries))
//   .append("path")
//     .attr('class', function(d) { console.log(d); return 'country ' + d.id; })
//     .attr("d", carto_countries.path);

// g.selectAll('.country')
//     .data(countries.features)
// .enter()
//     .append('path')
//         .attr('class', function(d) { return 'country ' + d.id; })
//         .attr('d', path);

// g.selectAll('.province')
//     .data(provinces.features)
//   .enter().append('path')
//     .attr('class', function(d) { if (d.id === 479613) {console.log(d);}return 'province ' + d.id; })
//     .attr('d', path);

// g.append('path')
//     .datum(topojson.mesh(data, data.objects.provinces, function(a, b) { return a !== b && a.id !== 'IRL'; }))
//     .attr('d', path)
//     .attr('class', 'subunit-boundary');
//
//
// g.selectAll('.province-label')
//     .data(provinces.features)
//   .enter().append('text')
//     .attr('class', function(d) { return 'province-label ' + d.id; })
//     .attr('transform', function(d) { return 'translate(' + path.centroid(d) + ')'; })
//     .attr('dy', '.35em')
//     .text(function(d) {return d.properties.name; });

// g.append('path')
//     .datum(countries)
//     .attr('d', carto_countries.path)
//     .attr('class', 'place');

// var ids = ['ESP', 'AFG', 'IRQ', 'CHN'];
// d3.selectAll('.country')
//     .filter(function(d, i) { return ids.indexOf(d.id ) !== -1; })
//     .attr('d', function(d, i){
//         console.log(i, data);
//     });
// g.selectAll('.place-label')
//     .data(countries.features)
// .enter().append('text')
//     .attr('class', 'place-label')
//     .attr('transform', function(d) { return 'translate(' + projection(d.geometry.coordinates) + ')'; })
//     .attr('x', function(d) { return d.geometry.coordinates[0] > -1 ? 6 : -6; })
//     .attr('dy', '.35em')
//     .style('text-anchor', function(d) { return d.geometry.coordinates[0] > -1 ? 'start' : 'end'; })
//     .text(function(d) { return d.properties.name; });
