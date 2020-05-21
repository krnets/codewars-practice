// 7kyu - What is type of variable?

/* Create a function to return true type of variable, i.e.

type([]) => 'array'
type({}) => 'object'
type('') => 'string'
type(NaN) => 'number' */

// function type(value) {
//     return Array.isArray(value) ? 'array' :
//         isNaN(value) && typeof value == 'number' ? 'number' :
//         /\d:\d{2}:\d{2}/.test(value) ? 'date' :
//         String(value) === value ? 'string' :
//         Number(value) === value ? 'number' :
//         value === null ? 'null' :
//         value === undefined ? 'undefined' :
//         'object'
// }

// function type(value) {
//     return {}.toString.call(value).slice(8, -1).toLowerCase();
// }

// const type = (value) => Object.prototype.toString.call(value).slice(8,-1).toLowerCase()

const type = value => ({}).toString.call(value).slice(8, -1).toLowerCase()

q = type([]) // 'array'
q
q = type({}) // 'object'
q
q = type('') // 'string'
q
q = type([].join()) // 'string'
q
q = type(new Date()) // 'date'
q
q = type(NaN) // 'number'
q