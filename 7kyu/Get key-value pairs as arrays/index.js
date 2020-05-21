// 7kyu - Get key/value pairs as arrays

/* Complete the keysAndValues function so that it takes in an object and returns the keys and values as separate arrays.
Style Points (JS/CoffeeScript only): This kata only tests for data that uses object literal notation (simple objects). 
For extra style, can you get your method to check for objects that extend their prototype? */

const keysAndValues = data => [Object.keys(data), Object.values(data)]

q = keysAndValues({ a: 1, b: 2, c: 3 }) 
q
//  [['a', 'b', 'c'], [1, 2, 3]]