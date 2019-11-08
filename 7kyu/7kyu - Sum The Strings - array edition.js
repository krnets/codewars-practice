// 7kyu - Sum The Strings: ARRAY EDITION

// function sumArr(a, b) {
//     for (var res = [], i = 0; i < a.length; i++)
//         res.push(String(Number(a[i]) + Number(b[i])))
//     return res
// }

const sumArr = (a, b) => a.map((v, i) => String(Number(v) + Number(b[i])))
// const sumArr = (a, b) => a.map((v, i) => '' + (+v + +b[i]))

// const sumArr = (a, b) => a.reduce((acc, v, i) => [...acc, String(Number(v) + Number(b[i]))], [])
// const sumArr = (a, b) => a.reduce((acc, v, i) => [...acc, '' + (+v + +b[i])], [])

q = sumArr(['4', '5', '6', '7', '8'], ['1', '2', '3', '4', '5'])
// ['5','7','9','11','13']
q

q = sumArr(['34', '5', '200', '17', '6'], ['27', '24', '14', '90', '16'])
// ['61', '29', '214', '107', '22']
q