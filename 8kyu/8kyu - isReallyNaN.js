// 8kyu - isReallyNaN

/* global isNaN function is returning true for undefined right now.
Write a function isReallyNaN that returns true only if passed in an argument that evalutes to NaN, and returns false otherwise.
Any solution is acceptable! */

// const isReallyNaN = val => typeof val == 'number' && isNaN(val)
// const isReallyNaN = Number.isNaN
const isReallyNaN = (val) => val != val

q = isReallyNaN(37) // false
q
q = isReallyNaN('37') // false
q
q = isReallyNaN(NaN) // true
q
q = isReallyNaN(undefined) // false
q