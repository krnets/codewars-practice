// Beta - Order by frequency

// function mostFrequent(arr, limit) {
//     let count = {}
//     arr.forEach(c => count[c] = (count[c] || 0) + 1)

//     let arrayFromMap = Object.keys(count).map(v => [v, count[v]])
//     let sortedByCount = arrayFromMap.sort((a, b) => b[1] - a[1])

//     return sortedByCount.slice(0, limit).reduce((a, b) => a.concat(b[0]), [])
// }

// const mostFrequent = (arr, limit) => {
//     let counts = {}
//     arr.forEach(ch => counts[ch] = (counts[ch] || 0) + 1)
//     let set = Object.keys(counts).sort((a, b) => counts[b] - counts[a])
//     return set.slice(0, limit)
// }

// function mostFrequent(arr, limit) {
//     return Object.keys(a = arr.reduce((x, y) => (x[y] = (x[y] || 0) + 1, x), {})).sort((x, y) => a[y] - a[x]).slice(0, limit)
// }

// function mostFrequent(arr, limit) {
//     return [...new Set(arr)].sort((a, b) => arr.filter(v => v == b).length - arr.filter(v => v == a).length).slice(0, limit)
// }

// const _ = require('lodash');

// mostFrequent = (arr, limit) => {
//     const counter = _.countBy(arr);
//     const sorted = _.orderBy(_.keys(counter), x => counter[x], 'desc');
//     return _.take(sorted, limit);
// }

// import { countBy, orderBy, keys, take } from 'lodash';

// const mostFrequent = (arr, limit) => {
//     const counter = countBy(arr);
//     const sorted = orderBy(keys(counter), x => counter[x], 'desc');
//     return take(sorted, limit);
// }


function mostFrequent(arr, limit) {
    let count = {}
    arr.forEach(c => count[c] = (count[c] || 0) + 1)
    return Object.keys(count).sort((a, b) => count[b] - count[a]).slice(0, limit)
}

let q = mostFrequent(['x', 'g', 'x', 't', 'g', 'x'], 2) // ['x','g']
q
q = mostFrequent(['c', 'b', 'b', 'a', 'a', 'a'], 3) // ['a','b','c']
q
q = mostFrequent(['k', 'j'], 1) // ['k']
q