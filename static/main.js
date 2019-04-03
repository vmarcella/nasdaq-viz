// custom javascript
$(function() {
    console.log('jquery is working')
    createGraph();
})

function createGraph() {
    const width = 960;
    const height = 700;
    const format = d3.format(",d"); // specify a decimal format that also allows values to be grouped by commas
    // Color scale generated from i want hue 
    const colors = d3.scaleOrdinal().range([
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
    const circleRadius = d3.scalePow().domain([-100, 100]).range([-50, 50]);

}
