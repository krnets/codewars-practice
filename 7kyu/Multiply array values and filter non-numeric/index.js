// 7kyu - Multiply array values and filter non-numeric

/* Your task is to write a function, which takes two arguments and returns an array. 
First argument is an array of values, second is multiplier. 
It should filter all non-numeric values and multiply the rest by given multiplier. */

// const multiplyAndFilter = (array, multiplier) => array.filter(v => typeof v == 'number').map(v => v * multiplier)
const multiplyAndFilter = (array, multiplier) => array.filter(Number.isFinite).map(v => v * multiplier)

q = multiplyAndFilter([1, 2, 3, 4], 1.5) // [1.5, 3, 4.5, 6]
q
q = multiplyAndFilter([1, 2, 3], 0) // [0, 0, 0]
q
q = multiplyAndFilter([0, 0, 0], 2) // [0, 0, 0]
q
q = multiplyAndFilter([1, null, function () {}, 2.5, 'string', 10, undefined, {},
    []
], 3) // [3,7.5,30]
q