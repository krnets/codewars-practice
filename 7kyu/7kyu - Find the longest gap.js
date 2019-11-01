// 7kyu - Find the longest gap

// function gap(num) {
//     let arr = num.toString(2).replace(/0+$/, '').split('1')
//         .filter(v => v)
//         .sort((a, b) => b.length - a.length)
//     return arr.length ? arr[0].length : 0
// }

// const gap = (num) => (num.toString(2).match(/10+(?=1)/g) || [' ']).sort().pop().length - 1

// function gap(num) {
//     return (num
//             .toString(2)
//             .match(/10+(?=1)/g) || [' '])
//                 .sort()
//                 .pop()
//                 .length - 1
// }

// const gap = num => num.toString(2)
//                        .split('1')
//                        .slice(0,-1)
//                        .reduce((p, c) => Math.max(p,c.length), 0);

const gap = num => num.toString(2).replace(/0+$/, '').split('1').reduce((prev, curr) => Math.max(prev, curr.length), 0)

// const gap = num => Math.max(...num.toString(2).replace(/0+$/g, '').split('1').map(gap => gap.length))

// function gap(num) {
//     return Math.max.apply(null, parseInt(num)
//         .toString(2)
//         .replace(/^0+|0+$/g, '')
//         .split('1')
//         .map(e => e.length)
//     )
// }

q = gap(9) // 2
q
q = gap(529) // 4
q
q = gap(20) // 1
q
q = gap(15) // 0
q