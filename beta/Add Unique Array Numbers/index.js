// Beta - Add Unique Array Numbers

/* To solve this kata you must traverse an array that could be multidimensional and turn it a single dimensional array. 
In other words flatten the array if needed. Then get rid of duplicate numbers, then add all the unique numbers 
in the array and return the sum. Assume that all numbers in the array are positive.

For example:

addUnique([1, 1, [2, 3, 1]]) -> // 6 */


// const _ = require('lodash')

// const addUnique = array => _.sum(_.uniq( _.flattenDeep(array)))
// const addUnique = array => _(array).flattenDeep().uniq().sum()

// const addUnique = arr => [...new Set([].concat(...arr.map(a => Array.isArray(a) ? [].concat(...a) : a)))].reduce((s, n) => s + n, 0)
// const addUnique = array => [...new Set(array.join(',').split(',').map(Number))].reduce((a, b) => a + b, 0)

const unique = arr => arr.filter((v, i) => arr.indexOf(v) == i)

const flatten = arr => arr.reduce((res, v) => res.concat(Array.isArray(v) ? flatten(v) : v), [])

const addUnique = array => unique(flatten(array)).reduce((a, b) => a + b, 0)


let q = addUnique([[1, 5, 3, 2, 4], [5, 4], [6], [1, 5, 3, 2, 4], [5, 4], [65]]) // 86
q
q = addUnique([1, 1, [1, 1, 1,[1, 1, 1], 1], 1, [1]]) // 1
q
q = addUnique([[1], [2], [3], [3]]) // 6
q