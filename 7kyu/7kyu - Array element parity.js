// 7kyu - Array element parity

// function solve(arr) {
//     let posInts = arr.filter((v, i) => v > 0 && arr.indexOf(v) == i)
//     let negInts = arr.filter((v, i) => v < 0 && arr.indexOf(v) == i)

//     let differencePos = posInts.filter(v => !negInts.includes(-v))
//     let differenceNeg = negInts.filter(v => !posInts.includes(-v))

//     return +differencePos ? +differencePos : +differenceNeg
// }

// function solve(arr) {
//     for (let i = 0; i < arr.length; i++)
//         if (arr.indexOf(-arr[i]) == -1)
//             return arr[i]
// }

// function solve(arr) {
//     for (let i = 0; i < arr.length; i++)
//         if (!arr.includes(-1 * arr[i]))
//             return arr[i]
// }

// const solve = arr => [...new Set(arr)].reduce((p, c) => p + c)
// const solve = arr => arr.filter(x => arr.indexOf(-x) == -1)[0]
// const solve = arr => arr.filter(x => !arr.includes(-x))[0]
const solve = arr => arr.find(v => !arr.includes(-v))

// const _ = require('lodash')
// const solve = _.flow(_.uniq, _.sum)

// import { flow, uniq, sum } from 'lodash'
// const solve = flow(uniq, sum);

q = solve([1, -1, 2, -2, 3]) // 3
q
q = solve([-3, 1, 2, 3, -1, -4, -2]) // -4
q
q = solve([1, -1, 2, -2, 3, 3]) // 3
q
q = solve([-110, 110, -38, -38, -62, 62, -38, -38, -38]) // -38
q
q = solve([-9, -105, -9, -9, -9, -9, 105]) // -9
q