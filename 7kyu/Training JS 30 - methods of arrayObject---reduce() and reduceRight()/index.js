// 7kyu - Training JS #30: methods of arrayObject---reduce() and reduceRight()

// function tailAndHead(arr) {
//     for (var out = [], i = 0; i < arr.length - 1; i++)
//         out.push(arr[i] % 10 + Number((arr[i + 1] + '')[0]))
//     return out.reduce((a, b) => a * b, 1)
// }

// const tailAndHead = arr => arr.map(String)
//     .reduce((x, y, i, r) => i ? x.concat(Number(r[i - 1][r[i - 1].length - 1]) + Number(y[0])) : x, [])
//     .reduce((a, b) => a * b)

// const tailAndHead = arr => arr.map((e, i) => +String(e)[String(e).length - 1] + +String(arr[i + 1])[0] || 1).reduce((a, b) => a * b)
// const tailAndHead = arr => arr.slice(1).map((x, i) => arr[i] % 10 + parseInt(x.toString().slice(0, 1))).reduce((a, b) => a * b)
// const tailAndHead = arr => arr.slice(1).map((x, i) => arr[i] % 10 + Number(String(x).slice(0, 1))).reduce((a, b) => a * b)

// const tailAndHead = arr => arr.slice(1).reduce((p, _, i) => p * (arr[i] % 10 + Number(arr[i + 1].toString()[0])), 1)
// const tailAndHead = arr => arr.slice(1).reduce((p, _, i) => p * (+(arr[i+1].toString()[0]) + arr[i] % 10), 1)
const tailAndHead = arr => arr.slice(1).reduce((p, _, i) => p * (+(String(arr[i + 1])[0]) + arr[i] % 10), 1)
// const tailAndHead = arr => arr.slice(1).reduce((p, n, i) => p * (+(arr[i] + '').slice(-1) + +(n + '')[0]), 1)
// const tailAndHead = arr => arr.slice(0, -1).reduce((p, n, i) => p * (+n.toString().slice(-1) + +arr[i + 1].toString()[0]), 1)

// const tailAndHead = arr => arr.reduce((p, c, i) => p * ((arr[i-1] % 10 || 0) + (i ? +String(c)[0] : 1)), 1)
// const tailAndHead = arr => arr.reduce((p, v, i) => i ? p * (+(v + '')[0] + arr[i - 1] % 10) : p, 1)
// const tailAndHead = arr => arr.reduce((p, v, i) => arr[i + 1] ? p * ((v % 10) + ~~('' + arr[i + 1])[0]) : p, 1)


q = tailAndHead([123, 456, 789, 12, 34, 56, 78]) // 532350
q
q = tailAndHead([1, 2, 3, 4, 5]) // 945
q
q = tailAndHead([111, 2345, 66, 78, 900]) // 7293
q
q = tailAndHead([35456, 782, 569, 2454, 875]) // 12012
q