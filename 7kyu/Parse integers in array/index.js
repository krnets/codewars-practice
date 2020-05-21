// 7kyu - Parse integers in array

/* A colleague asked if you can help him fix his function. It seems it doesn't always parse Integers correctly.

Bugs | Numbers | Arrays | Functional Programming | Declarative Programming | Utilities */

/**
 * Function converts array of string to array of integers.
 * @param  {Array} of numbers in form of string
 * @return {Array} of integer numbers 
 */

// var parseNumbers = function (intStrs) {
//     return (intStrs.some(v => v < 0)) ?
//         intStrs.map(v => +Number(Math.ceil(v)).toFixed()) :
//         intStrs.map(v => +Number(Math.floor(v)).toFixed())
// }

var parseNumbers = function (intStrs) {
    return intStrs.map(v => parseInt(v));
}

// const parseNumbers = intStrs => intStrs.map(v => v | 0)


q = parseNumbers([]) // []
q
q = parseNumbers(['13']) // [13]
q
q = parseNumbers(['2.48']) // [2]
q
q = parseNumbers(['10']) // should return [10]
q
q = parseNumbers(['-1', '0', '1']) // should return [-1,0,1]
q