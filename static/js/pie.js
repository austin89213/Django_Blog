


var post = Number(document.getElementById("post-viewd").innerHTML);
console.log(typeof(post));
var comment = {
    name: "留言",
    value: Number(document.getElementById("comments").innerHTML)
};
var uncomment = {
    name: "僅觀看未留言 ",
    value: post-comment.value
};
/*------set value here-----*/
//change data to pie
var dataset = [comment,uncomment];
var pie = d3.pie()
            .value(d => d.value);
console.log(pie(dataset));


var width = 250, height = 250;

//set the pie radius
var arc = d3.arc()
        .innerRadius(0)
        .outerRadius(width / 2 - 1);

//set the text in pie radius
var arcLabel = d3.arc().innerRadius(width / 2 * 0.5).outerRadius(width / 2 * 0.8);

//set color
var color = d3.scaleOrdinal()
                .domain(dataset.map(d => d.name))
                .range(d3.quantize(t => d3.interpolateSpectral(t * 0.8 + 0.1), dataset.length).reverse());

//set svg
const svg = d3.select('#chart')
            .append('svg')
            .attr("viewBox", [-width / 2, -height / 2, width * 2 , height * 2]);

var g = svg.selectAll(".arc")
            .data(pie(dataset))
            .enter().append("g")
            .attr("class", "arc");

//draw pie and set color
g.append("path")
    .attr("d", arc)
    .style("fill", function(d) {
        return color(d.data.value);
    });

//set the data value as text with some font attribute
g.append("text")
    .attr("transform", d => `translate(${arcLabel.centroid(d)})`)
    .call(text => text.append("tspan")
        .attr("x", "-0.3em")
        .attr("y", "0.2em")
        .attr("font-size", "0.8em")
        .attr("font-weight", "bold")
        .text(d => d.data.value))
//set the data name as text with some font attribute
    .call(text => text.append("tspan")
        .attr("x", "-1.3em")
        .attr("y", "-1.3em")
        .attr("font-size", "0.7em")
        .attr("fill-opacity", 0.7)
        .text(d => d.data.name));
