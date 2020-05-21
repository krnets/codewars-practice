// 7kyu - Multidimensional array

// const getElement = (array, indexes) => eval('array' + '[' + indexes.map(v => [v]).join('][') + ']')
const getElement = (array, indexes) => eval(`array[${ indexes.map(v => [v]).join('][') }]`)

// const getElement = (array, indexes) => indexes.reduce((a, i) => a[i], array)

// const getElement = require('lodash/get')

// function getElement(a, b) {
//     for (let x of b) a = a[x]
//     return a
// }

q = getElement([[1, 2], [3, 4], [5, 6]], [0,0]) // 1
q
q = getElement(['one','two','three'], [2]) // 'three'
q
q = getElement([[[ 1, 2, 3]]], [ 0, 0, 1 ]) // 2
q