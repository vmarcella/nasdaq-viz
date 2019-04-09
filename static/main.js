// custom javascript
$(function() {
  console.log("jquery is working");
  createGraph();
});

function createGraph() {
  const width = 1400;
  const height = 900;
  const format = d3.format(",d"); // specify a decimal format that also allows values to be grouped by commas
  // Color scale generated from i want hue (need 20 colors)
  const colors = d3
    .scaleOrdinal()
    .range([
      "#56c19e",
      "#d34092",
      "#49b94f",
      "#a54fb7",
      "#adb639",
      "#7264d4",
      "#86b75b",
      "#da7cc9",
      "#557e30",
      "#5675c0",
      "#d69d36",
      "#4facd8",
      "#c9522b",
      "#37845f",
      "#cd3e54",
      "#8d7c38",
      "#ac8dcd",
      "#c78151",
      "#9e4b6f",
      "#db7a80"
    ]);

  // Create a scaling function
  const getCircleRadius = d3
    .scalePow()
    .domain([0, 400])
    .range([0, 75]);

  // Construct the svg to render the drawing to
  const svg = d3
    .select("#chart")
    .append("svg")
    .attr("width", width)
    .attr("height", height)
    .attr("class", "bubble");

  // Fetch the stock data to plot to the svg
  d3.json("/get_stocks").then(function(quotes) {
    console.log(quotes.children[0]["lastsale"]);
    const nodes = d3.hierarchy(quotes).sum(function(stock) {
      return Number(stock["lastsale"]);
    });

    // D3 version 5.0 uses d3.pack() instead of d3.layout.pack()
    const bubble = d3
      .pack(quotes)
      .size([width, height])
      .padding(1)
      .radius(function(d) {
        console.log("inside the bubble");
        console.log(d);
        return 5 + getCircleRadius(d.value / 2) * 1;
      });

    const node = svg
      .selectAll(".node")
      .data(bubble(nodes).descendants())
      .enter()
      .filter(function(node) {
        return !node.children;
      })
      .append("g")
      .attr("class", "node")
      .attr("transform", function(data) {
        return "translate(" + data.x + "," + data.y + ")";
      });

    node
      .append("circle")
      .attr("r", function(data) {
        console.log(data);
        return data.r;
      })
      .attr("fill", function(data, extra) {
        console.log(data);
        console.log(extra);
        return colors(extra);
      });

    node
      .append("text")
      .attr("dy", ".3em")
      .style("text-anchor", "middle")
      .text(function(data) {
        return data.data.symbol;
      });
  });
}
