// 7kyu - Easy mathematical callback

/* Write the processArray function, which takes an array and a callback function as parameters. 
The callback function can be, for example, a mathematical function that will be applied on each element of this array.

1) Array [4, 8, 2, 7, 5] after processing with function
myArray = processArray(myArray, function (a) { return a * 2; });
will be [ 8, 16, 4, 14, 10 ].

2) Array [7, 8, 9, 1, 2] after processing with function
myArray = processArray(myArray, function (a) { return a + 5; });
will be [ 12, 13, 14, 6, 7 ]. */

const processArray = (arr, callback) => arr.map(v => callback(v))
// const processArray = (arr, callback) => arr.map(callback)

q = myArray = [4, 8, 2, 7, 5] 
q
q = processArray(myArray, function(a) { return a * 2})  // [ 8, 16, 4, 14, 10 ]
q

q = myArray = [7, 8, 9, 1, 2] 
q
q = processArray(myArray, function(a) { return a + 5})  // [ 12, 13, 14, 6, 7 ]
q