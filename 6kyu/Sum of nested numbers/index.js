// 6kyu - Sum of nested numbers

/* Build a function sumNestedNumbers that finds the sum of all numbers in a series of nested arrays 
raised to the power of their respective nesting levels. 
Numbers in the outer most array should be raised to the power of 1.

sumNestedNumbers([1, [2], 3, [4, [5]]])

should return 1 + 2*2 + 3 + 4*4 + 5*5*5 === 149 */

// function sumNestedNumbers(arr) {
//     let res = []
//     let flatten = (arr, exp) => (++exp, arr.map(v => Array.isArray(v) ? flatten(v, exp) : res.push([v, exp])))
//     flatten(arr, 0)
//     return res.reduce((acc, [v, exp]) => acc + Math.pow(v, exp), 0)
// }

// const sumNestedNumbers = (arr, pow = 1) => arr.reduce((s, a) => s + (a.reduce ? sumNestedNumbers(a, pow + 1) : Math.pow(a, pow)), 0)

const sumNestedNumbers = (arr, exp = 1) => arr.reduce((sum, v) => sum + (v.length ? sumNestedNumbers(v, exp + 1) : Math.pow(v, exp)), 0)

q = sumNestedNumbers([1, [2], 3, [4, [5]]]) // 149
q