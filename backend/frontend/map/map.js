/* jshint undef: true, unused: true */
/* globals d3 */
var width = 800,
    height = 800;

var projection = d3.geo.mercator()
    .center([0, 0])
    // .rotate(180)
    // .parallels([50, 60])
    // .scale(860)
    .translate([width / 2, height / 2]);

var path = d3.geo.path()
    .projection(projection)
    .pointRadius(2);

// normalize the scale to positive numbers
var scale = d3.scale.linear()
    .range([1, 100]);

var POPkeys = {};
var svg = d3.select('body')
        .append('svg')
        .attr('width', width)
        .attr('height', height);

var g = svg.append('g');

// SOURCE: http://th-mayer.de/cartogram
var carto_countries = d3.cartogram()
    .projection(projection)
    .properties(function(d) {
        return POPkeys[d.id];
    })
    .value(function(d) {
        var x = (POPkeys[d.id] !== undefined? POPkeys[d.id]: 0);
        // console.log(x);
        return scale(x);
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

var years = [
    2001, 2003, 2005, 2007
];


var alphas = [
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 'Inf'
];


d3.json('world.json', function(error, data) {
    d3.json("diversity10Alpha.json", function(error, resistanceData) {
        var year = 2001;
        var alpha = '0';

        function updateData (resistanceData, year, alpha){
            var values = d3.entries(resistanceData)
                .map(function(d) {
                    if (year in d['value']){
                        POPkeys[d['key']] = d['value'][year][alpha];
                        return +d['value'][year][alpha];
                    }
                })
                .filter(function(n) {
                    return !isNaN(n);
                })
                .sort(d3.ascending);
            return values;
        }

        function updateViz(resistanceData, data, year, alpha) {
            console.log(year, alpha);
            var features = carto_countries(data, data.objects.worldcountries).features;
            var values = updateData(resistanceData, year, alpha);
            var min = 0;
            var max = values[values.length - 1];
            scale.domain([min, max]);
            color.domain([min, max]);
            console.log(min, max);
            var countries = g.selectAll("path")
                .data(features);
            countries.transition()
              .duration(1000)
              .ease("linear")
              .attr("fill", function(d) {
                return color(+d.properties);
              })
              .attr("d", carto_countries.path);
        }

        var yearSelect = d3.select('#year')
                .on('change', function(e) {
                    year = years[this.selectedIndex];
                    updateViz(resistanceData, data, year, alpha);
                    // location.hash = '#' + [year.id].join("/");
                });

        yearSelect.selectAll("option")
          .data(years)
          .enter()
          .append("option")
            .attr("value", function(y) { return y; })
            .text(function(y) { return y; })

        var alphaSelect = d3.select("#alpha")
            .on("change", function(e) {
                alpha = alphas[this.selectedIndex];
                updateViz(resistanceData, data, year, alpha);
                // location.hash = "#" + [alpha.id].join("/");
            });

        alphaSelect.selectAll("option")
          .data(alphas)
          .enter()
          .append("option")
            .attr("value", function(y) { return y; })
            .text(function(y) { return y; })


         var values = updateData(resistanceData, year, alpha);
          var min = 0;
          var max = values[values.length - 1];
          scale.domain([min, max]);
          color.domain([min, max]);

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
