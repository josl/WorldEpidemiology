var margin = {
        top: 20,
        right: 20,
        bottom: 30,
        left: 40
    },
    width = 960 - margin.left - margin.right,
    height = 500 - margin.top - margin.bottom;

var x = d3.scale.linear()
    .range([0, width]);

var y = d3.scale.linear()
    .range([height, 0]);

var svg = d3.select("body")
    .append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

var attribute = 'SP-DYN-TFRT-IN';

d3.json("/api/Spain", function (error, data) {
    console.log(data);

    // Coerce the data to numbers.
    data.forEach(function (d) {
        d.date = +d.date;
        console.log(d);
        if (attribute in d.attrs) {
            d.data = +d.attrs[attribute]['value'];
            console.log(d.data, d.date);
        }
    });

    // Compute the scales’ domains.
    x.domain(d3.extent(data, function (d) {
        return d.date;
    }))
    .nice();
    y.domain(d3.extent(data, function (d) {
        return d.data;
    }))
    .nice();

    svg.append("text")
        .attr("class", "title")
        .attr("x", x(1961))
        .attr("y", y(1.6))
        .text("Fertility rate in Spain");
    svg.append("text")
        .attr("class", "title")
        .attr("x", x(1961))
        .attr("y", y(1.5))
        .text("(total births per woman)");


    // Add the x-axis.
    svg.append("g")
        .attr("class", "x axis")
        .attr("transform", "translate(0," + height + ")")
        .call(d3.svg.axis()
            .scale(x)
            .orient("bottom"));

    // Add the y-axis.
    svg.append("g")
        .attr("class", "y axis")
        .call(d3.svg.axis()
            .scale(y)
            .orient("left"));

    // Add the points!
    svg.selectAll(".point")
        .data(data)
        .enter()
        .append("circle")
        .attr("class", "point")
        .attr("r", 4.5)
        .attr("cx", function (d) {
            return x(d.date);
        })
        .attr("cy", function (d) {
            console.log(d.data);
            return y(d.data);
        });

});
