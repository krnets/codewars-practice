// 6kyu - Throwing Darts

/* You've just recently been hired to calculate scores for a Dart Board game!

Scoring specifications:

    0 points - radius above 10
    5 points - radius between 5 and 10 inclusive
    10 points - radius less than 5

If all radiuses are less than 5, award 100 BONUS POINTS!

Write a function that accepts an array of radiuses (can be integers and/or floats), and returns a total score using the above specification.

An empty array should return 0.
Examples:

scoreThrows( [1, 5, 11] )    =>  15
scoreThrows( [15, 20, 30] )  =>  0
scoreThrows( [1, 2, 3, 4] )  =>  140   */

function scoreThrows(radiuses) {
    let points = radiuses.map(v => v > 10 ? 0 : v >= 5 ? 5 : 10).reduce((a, b) => a + b, 0)
    let bonus = radiuses.every(v => v < 5)
    return radiuses.length && bonus ? 100 + points : points
}


q = scoreThrows([1, 5, 11]) // 15
q
q = scoreThrows([1, 3, 4]) // 15
q
q = scoreThrows([]) // 0
q