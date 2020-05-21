// 7kyu - Flatten

// Write a function that flattens an Array of Array objects into a flat Array. 
// Your function must only do one level of flattening.

// const flatten = array => array.reduce((a, b) => a.concat(b), [])

const flatten = array => [].concat(...array)

// var flatten = function (array){
//     return [].concat.apply([],array);
// }

// var flatten = function (array){
//     return Array.prototype.concat.apply([],array);
// }

q = flatten([]), []
q
q = flatten([1, 2, 3]), [1, 2, 3]
q
q = flatten([[1, 2, 3], ["a", "b", "c"], [1, 2, 3]]), [1, 2, 3, "a", "b", "c", 1, 2, 3]
q
q = flatten([[3, 4, 5], [[9, 9, 9]], ["a,b,c"]]), [3, 4, 5, [9, 9, 9], "a,b,c"]
q
q = flatten([[[3], [4], [5]], [9], [9], [8], [[1, 2, 3]]]), [[3], [4], [5], 9, 9, 8, [1, 2, 3]]
q