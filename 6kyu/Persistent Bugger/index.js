// 6kyu - Persistent Bugger

// function persistence(num) {
//     if (String(num).length < 2) return 0

//     let count = len = 0

//     while (len != 1) {
//         num = [...String(num)].reduce((a, b) => a * Number(b))
//         len = [...String(num)].length
//         count++
//     }
//     return count
// }

// function persistence(num) {
//     let count = 0
//     let n = [...String(num)]

//     while (n.length > 1) {
//         n = [...String(n.reduce((a, b) => a * Number(b)))]
//         count++
//     }
//     return count
// }

// const persistence = num => {
//     return `${num}`.length > 1 
//       ? 1 + persistence(`${num}`.split('').reduce((a, b) => a * +b)) 
//       : 0;
//   }

// const persistence = num => String(num).length > 1 ? 1 + persistence([...String(num)].reduce((a, b) => a * Number(b))) : 0
const persistence = num => String(num).length > 1 ? 1 + persistence([...String(num)].reduce((a, b) => a * b)) : 0

q = persistence(39) // 3
q
q = persistence(4) // 0
q
q = persistence(25) // 2
q
q = persistence(999) // 4
q