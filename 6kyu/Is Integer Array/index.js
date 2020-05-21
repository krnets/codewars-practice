// 6kyu - Is Integer Array ?

// const isIntArray = arr => !!arr && arr.every(v => Number.isInteger(v))
// const isIntArray = arr => !!arr && arr.every(Number.isInteger)
// const isIntArray = arr => !!arr && arr.every(x => ~~x === x)
const isIntArray = arr => Array.isArray(arr) && arr.every(Number.isInteger)

q = isIntArray([]) // true, "Input: []"
q
q = isIntArray([1, 2, 3, 4]) // true, "Input: [1, 2, 3, 4]"
q
q = isIntArray([1, 2, 3, NaN]) // false, "Input: [1, 2, 3, NaN]"
q