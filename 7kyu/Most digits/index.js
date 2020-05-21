// 7kyu - Most digits

/* Find the number with the most digits.
If two numbers in the argument array have the same number of digits, return the first one in the array. */

// function findLongest(array) {
//     let numberOfDigits = array.map(v => [s = [...String(v)], s.length])
//     let sortedByArrayLength = numberOfDigits.sort((a, b) => b[1] - a[1])
//     return Number(sortedByArrayLength[0][0].join ``)
// }
// const findLongest = l => l.reduce((a, b) => (`${b}`.length > `${a}`.length) ? b : a)
// const findLongest = array => array.reduce((prev, curr) => String(prev).length < String(curr).length ? curr : prev)
const findLongest = arr => arr.sort((a, b) => (b + '').length - (a + '').length)[0]

q = findLongest([1, 10, 100]) // 100
q
q = findLongest([9000, 8, 800]) // 9000
q
q = findLongest([8, 900, 500]) // 900
q