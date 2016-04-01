var width = 960,
    height = 960;

var projection = d3.geo.mercator()
    // .center([200, 55.4])
    .rotate([4.4, 0])
    //.parallels([50, 60])
    .scale(900 * 0.5)
    .translate([width / 2, height / 2]);


var path = d3.geo.path()
    .projection(projection)
    .pointRadius(2);

var zoom = d3.behavior.zoom()
    .scaleExtent([1, 8])
    .on("zoom", zoomed);

var path = d3.geo.path()
    .projection(projection);

var svg = d3.select("body").append("svg")
    .attr("width", width)
    .attr("height", height)
  .append("g");

var g = svg.append("g");

svg.append("rect")
    .attr("class", "overlay")
    .attr("width", width)
    .attr("height", height);

    svg
        .call(zoom)
        .call(zoom.event);


d3.json("topoDB.json", function(error, data) {
    console.log(data);
  var provinces = topojson.feature(data, data.objects.provinces),
      countries = topojson.feature(data, data.objects.countries);
  console.log(countries);
  console.log(provinces);

  g.selectAll(".country")
      .data(countries.features)
    .enter().append("path")
      .attr("class", function(d) { return "country " + d.id; })
      .attr("d", path);

    g.selectAll(".province")
        .data(provinces.features)
      .enter().append("path")
        .attr("class", function(d) { if (d.id === 479613) {console.log(d);}return "province " + d.id; })
        .attr("d", path);

  g.append("path")
      .datum(topojson.mesh(data, data.objects.provinces, function(a, b) { return a !== b && a.id !== "IRL"; }))
      .attr("d", path)
      .attr("class", "subunit-boundary");


  g.selectAll(".province-label")
      .data(provinces.features)
    .enter().append("text")
      .attr("class", function(d) { return "province-label " + d.id; })
      .attr("transform", function(d) { return "translate(" + path.centroid(d) + ")"; })
      .attr("dy", ".35em")
      .text(function(d) {return d.properties.name; });

  g.append("path")
      .datum(countries)
      .attr("d", path)
      .attr("class", "place");

  g.selectAll(".place-label")
      .data(countries.features)
    .enter().append("text")
      .attr("class", "place-label")
      .attr("transform", function(d) { return "translate(" + projection(d.geometry.coordinates) + ")"; })
      .attr("x", function(d) { return d.geometry.coordinates[0] > -1 ? 6 : -6; })
      .attr("dy", ".35em")
      .style("text-anchor", function(d) { return d.geometry.coordinates[0] > -1 ? "start" : "end"; })
      .text(function(d) { return d.properties.name; });
});


function zoomed() {
  g.attr("transform", "translate(" + d3.event.translate + ")scale(" + d3.event.scale + ")");
}
