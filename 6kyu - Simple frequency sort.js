// 6kyu - Simple frequency sort

// function solve(arr) {
//     let count = {}
//     arr.forEach(n => !!count[n] ? count[n]++ : count[n] = 1)
//     return arr.sort((a, b) => count[a] !== count[b] ? count[b] - count[a] : a - b)
// }

function solve(arr) {
    let count = {}
    arr.forEach(n => count[n] = (count[n] || 0) + 1)
    return arr.sort((a, b) => count[b] - count[a] || a - b)
}

// function solve(arr) {
//     let dict = arr.reduce((a, b) => (a[b] = a[b] + 1 || 1, a), {})
//     return arr.sort((a, b) => dict[b] - dict[a] || a - b)
// }

// function solve(arr) {
//     let r = {}
//     for (let n of arr)
//         r[n] = r[n] + 1 || 1
//     return arr.slice().sort((a, b) => r[b] - r[a] || a - b)
// }

// const R = require('ramda');

// function solve(xs) {
//     const fs = R.countBy(R.identity, xs);
//     return R.sortWith([R.descend(x => fs[x]), R.ascend(x => x)], xs);
// }

// const _ = require('lodash');

// function solve(xs) {
//     return _.orderBy(xs, [_.propertyOf(_.countBy(xs)), _.identity], ['desc', 'asc']);
// }

// import { orderBy, propertyOf, countBy, identity } from 'lodash'

// function solve(xs) {
//     return orderBy(xs, [propertyOf(countBy(xs)), identity], ['desc', 'asc']);
// }

// function solve(arr) {
//     return arr.map(elem => [elem, arr.filter(n => n == elem).length])
//               .sort((a, b) => b[1] - a[1] || a[0] - b[0])
//               .map(x => x[0])
// }


q = solve([2, 3, 5, 3, 7, 9, 5, 3, 7]) // [3,3,3,5,5,7,7,2,9]
q
q = solve([1, 2, 3, 0, 5, 0, 1, 6, 8, 8, 6, 9, 1]) // [1,1,1,0,0,6,6,8,8,2,3,5,9]
q
q = solve([5, 9, 6, 9, 6, 5, 9, 9, 4, 4]) // [9,9,9,9,4,4,5,5,6,6]
q
q = solve([4, 4, 2, 5, 1, 1, 3, 3, 2, 8]) //[1,1,2,2,3,3,4,4,5,8]
q
q = solve([4, 9, 5, 0, 7, 3, 8, 4, 9, 0]) // [0,0,4,4,9,9,3,5,7,8]
q