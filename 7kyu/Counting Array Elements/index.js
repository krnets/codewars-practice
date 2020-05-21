// 7kyu - Counting Array Elements

// function count(array) {
//     let counter = {}

//     array.reduce((counter, letter) => { 
//         !counter[letter] ? counter[letter] = 1 : counter[letter]++; 
//         return counter }, counter)

//     return counter
// }

// const count = array => array.reduce((counter, letter) => { 
//         !counter[letter] ? counter[letter] = 1 : counter[letter]++; 
//         return counter}, {})


// function count(array) {
//     const dict = {}
//     for (let key of array) {
//         if (key in dict)
//             dict[key]++
//         else
//             dict[key] = 1
//     }
//     return dict
// }

// const { countBy: count } = require('lodash');

// const count = array => array.reduce((c, l) => (c[l] = (c[l] || 0) + 1, c), {})
// const count = array => array.reduce((c, l) => ((c[l] = c[l] + 1 || 1), c), {})
const count = array => array.reduce((c, l) => (c[l] = ++c[l] || 1, c), {})

// function count(array) {
//     let counter = {}
//     array.forEach(item => {
//         counter[item] = (counter[item] || 0) + 1
//     })
//     return counter
// }

// const count = (array, r = {}) => array.forEach(c => r[c] ? r[c]++ : r[c] = 1) || r


q = count(['a', 'a', 'b', 'b', 'b']) // { 'a': 2, 'b': 3 }
q