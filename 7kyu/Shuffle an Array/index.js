// 7kyu - Shuffle an Array

/* Write a function to shuffle an array.

Input: [1,2,3,4]
Output: [3,1,4,2]

Assume input is array.
Hint: Math.random()

http://devdocs.io/javascript/global_objects/math/random
Fundamentals | Loops | Control Flow | Basic Language Features | Algorithms */

// function shuffle(arr) {
//     let res = []
//     while (res.length < arr.length) {
//         let random = ~~(Math.random() * arr.length)
//         if (!res.includes(random))
//             res.push(random)
//     }
//     return res.map(v => arr[v])
// }

// const shuffle = require('lodash').shuffle;
// import { shuffle } from 'lodash';

const shuffle = arr => arr.sort(() => .5 - Math.random())
// const shuffle = arr => arr.sort((a, b) => Math.random() > 0.5 ? 1 : -1)

/**
 * Fisher–Yates Shuffle
 */

// function shuffle(array) {
//     let i = array.length, j;
//     while (i) {
//         j = Math.random() * i-- | 0;
//         [array[i], array[j]] = [array[j], array[i]];
//     }
//     return array;
// }

q = shuffle([1, 2, 3, 4]) // [3,1,4,2]
q
q = shuffle([5, 6, 7, 8]) // [8,5,7,6]
q