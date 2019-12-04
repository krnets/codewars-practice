// Beta - Interweaving an Array

/* Given two arrays, interweave them by alternating an element form the array and then one from the second array;

[4, 5, 6] [1, 2, 3] => [4, 1, 5, 2, 6, 3]

The arrays can be of any length, and contain any data type.

[1,2,3] [4] => [1,4,2,3]
[1] [2,3,4] => [1,2,3,4]

Algorithms | Arrays */


function interweave(arr1, arr2) {
    let res = []
    let len = Math.max(arr1.length, arr2.length)
    for (let i = 0; i < len; i++) {
        if (arr1.length > 0) res.push(arr1.shift())
        if (arr2.length > 0) res.push(arr2.shift())
    }
    return res
}

// function interweave(arr1, arr2) {
//     let res = []
//     while (arr1.length + arr2.length > 0) {
//         if (arr1.length > 0) res.push(arr1.shift())
//         if (arr2.length > 0) res.push(arr2.shift())
//     }
//     return res
// }

// const interweave = (a, b) => [...Array(Math.max(a.length, b.length))]
//     .reduce((res, x) => res.concat(a.length ? [a.shift()] : []).concat(b.length ? [b.shift()] : []), []);

// const _ = require('lodash')
// const interweave = (a, b) => _.compact(_.flatten(_.zip(a, b)))  // fails advanced test on Codewars, but works nevertheless

// import { compact, flatten, zip } from 'lodash'
// const interweave = (a, b) => compact(flatten(zip(a, b)))  // fails advanced test on Codewars, but works nevertheless

// const _ = module.require('lodash');

// function interweave(a1, a2) {
//     const a = x => [x];
//     return _(_.map(a1, a)).zip(_.map(a2, a)).flatten().compact().flatten().value();
// }

// import _, { map } from 'lodash';

// function interweave(a1, a2) {
//     const a = x => [x];
//     return _(map(a1, a)).zip(map(a2, a)).flatten().compact().flatten().value();
// }


let q = interweave([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]) // [ 1, 1, 2, 2, 3, 3, 4, 4, 5, 5 ]
q
q = interweave(["string", 35], [90, 't', 23]) // [ 'string', 90, 35, 't', 23 ]
q
q = interweave([90, 't', 23], ["string", 35]) // [ 90, 'string', 't', 35, 't', 23 ]
q