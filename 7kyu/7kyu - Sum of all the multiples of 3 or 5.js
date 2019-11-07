// 7kyu - Sum of all the multiples of 3 or 5


// const findSum = n => Array(n).fill().map((_, i) => i + 1).filter(v => v % 3 == 0 || v % 5 == 0).reduce((a, b) => a + b)
// const findSum = n => Array(n).fill().map((_, i) => i + 1).filter(v => !(v % 3 && v % 5)).reduce((a, b) => a + b)
// const findSum = n => Array(n).fill().map((_, i) => i + 1).reduce((acc, cur, i, a) => !(cur % 3 && cur % 5) ? acc += cur : acc, 0)
// const findSum = n => [...Array(n + 1).keys()].filter(cur => cur % 3 === 0 || cur % 5 === 0).reduce((acc, cur) => acc + cur, 0);
// const findSum = n => [...Array(n + 1).keys()].filter(v => !(v % 3 && v % 5)).reduce((a, b) => a + b)
// const findSum = n => [...Array(n)].map((_, i) => ++i).reduce((r, e) => r + (e % 5 && e % 3 ? 0 : e), 0)
const findSum = n => [...Array(n+1).keys()].reduce((a, b) => a + (b % 3 && b % 5 ? 0 : b))


// function findSum(n) {
//     for (var sum = 0, i = 0; i <=n; i++)
//         if (i % 3 == 0 || i % 5 == 0)
//             sum += i
//     return sum
// }

q = findSum(5) // 8
q
q = findSum(10) // 33
q