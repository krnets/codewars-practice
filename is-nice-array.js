// const isNice = (arr) => arr.map(v => arr.includes(v + 1) || arr.includes(v - 1)).every(v => v)
// const isNice = (arr) => !!arr.length && arr.map(v => arr.includes(v + 1) || arr.includes(v - 1)).filter(v => v == false).length == 0
// const isNice = (arr) => arr.length > 0 && arr.map(v => arr.includes(v + 1) || arr.includes(v - 1)).filter(v => v == false).length == 0
// const isNice = (arr) => !!arr.length && arr.every(x => arr.some(y => y == x - 1 || y == x + 1))
// const isNice = arr => arr.length > 0 && arr.every(el => arr.some(x => Math.abs(el - x) == 1))
const isNice = arr => !arr || !arr.length ? false : arr.every(el => arr.some(x => Math.abs(el - x) == 1))

q = isNice([2, 10, 9, 3]) // true
q
q = isNice([3, 4, 5, 7]) // false
q
q = isNice([]) // false
q
q = isNice() // false
q