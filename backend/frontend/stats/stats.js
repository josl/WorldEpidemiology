/* globals d3, ss */

d3.json("/api/all", function (error, data) {
    console.log(data);
    // Coerce the data to numbers.
    var hist = {};
    data.forEach(function (d) {
        d.date = +d.date;
        d['fertility_rate,_total_(births_per_woman)'] = +d['fertility_rate,_total_(births_per_woman)'];
        var dat = d['fertility_rate,_total_(births_per_woman)'];
        if (!isNaN(dat)){
            hist[dat] = hist[dat] ? hist[dat] + 1 : 0;
        }
    });
    var values = d3.keys(hist);
    values = values.map(function(d){
        return +d;
    });
    console.log(ss.mean(values));
    console.log(ss.variance(values));
    console.log(ss.standardDeviation([5,4,6,39]));
});
