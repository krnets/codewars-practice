// 7kyu - Filter Coffee

// return array of prices that are within budget
const search = (budget, prices) => prices.filter(v => v <= budget).sort((a, b) => a - b).toString()

// "Should filter out the prices outside budget"
q = search(3, [6, 1, 2, 9, 2]) // "1,2,2"
q

// "Should filter out the prices outside budget"
q = search(14, [7, 3, 23, 9, 14, 20, 7]) // "3,7,7,9,14"
q

// "Should return an empty string when budget is zero"
q = search(0, [6, 1, 2, 9, 2]) // ""
q