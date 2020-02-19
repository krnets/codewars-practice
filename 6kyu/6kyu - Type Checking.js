// 6kyu - Type Checking

/* Create the function type which takes the argument val and returns val's type as a string. If possible, type should return additional information. Instead of a wall of text, here are code examples:

type(undefined) --> 'Undefined'
type(null) --> 'Null'
type(true) --> 'Boolean'
type(function(){}) --> 'Function'
type(Math.max) --> 'Function'
type('abc') --> 'String'
type({snap: "crackle"}) --> 'Object'

//Numbers should include additional information
type(1) --> 'Number Integer'
type(1.1) --> 'Number Float'
type(NaN) --> 'Number NaN'
type(-Infinity) --> 'Number Infinite'

//If a string is numeric-formatted:
type('123')
type('123.321')
type('0xF')
  --> All return 'String Numeric'

//For constructed objects, return the name of the constructor
type(/abc/) --> 'RegExp'
type([1,2,3]) --> 'Array'
function Custom(){}
type(new Custom()) --> 'Custom' */

// function type(val) {
//     if (typeof val === 'undefined') return 'Undefined'
//     if (typeof val === 'object' && val === null) return 'Null'
//     if (typeof val === 'boolean') return 'Boolean'
//     if (typeof val === 'function') return 'Function'
//     if (typeof val === 'string' && !isNaN(parseInt(val))) return 'String Numeric'
//     if (Number.POSITIVE_INFINITY == val || Number.NEGATIVE_INFINITY == val) return 'Number Infinite'
//     if (typeof val === 'number' && Number.isInteger(val)) return 'Number Integer'
//     if (typeof val === 'number' && Number.isNaN(val)) return 'Number NaN'
//     if (typeof val === 'number' && parseInt(val) === val) return 'Number'
//     if (typeof val === 'number' && parseFloat(val) === val) return 'Number Float'
//     return val.constructor.toString().match(/function (.+)\(/)[1]
// }

function type(val) {
    if (val === undefined) return 'Undefined'
    if (val === null) return 'Null'
    let T = val.constructor.name
    if (T == 'String' && !isNaN(val)) return 'String Numeric'
    if (T != 'Number') return T
    if (Number.isNaN(val)) return 'Number NaN'
    if (Number.isInteger(val)) return 'Number Integer'
    if (Number.isFinite(val)) return 'Number Float'
    return 'Number Infinite'
}

q = type(/a/) // "RegExp"
q
q = type({
    snap: "crackle"
}) // "Object"
q
q = type('abc') // "String"
q

function Custom() {}
q = type(new Custom()) // "Custom"
q

q = type('123') // "String Numeric"
q
q = type('123.321') // "String Numeric"
q
q = type('0xF') // "String Numeric"
q
q = type([1]) // "Array"
q
q = type(undefined) // "Undefined"
q
q = type(null) // "Null"
q
q = type(true) // "Boolean"
q
q = type(function () {}) // "Function"
q
q = type(Math.max) // "Function"
q

q = type(1) // "Number Integer"
q
q = type(1.1) // "Number Float"
q
q = type(NaN) // "Number NaN"
q
q = type(-Infinity) // "Number Infinite"
q