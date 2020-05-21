// 7kyu - Make a square box!

// function box(n) {
//     let a = '-'.repeat(n)
//     if (n > 2) {
//         let b = '-' + ' '.repeat(n - 2) + '-'
//         return [
//             [a], Array(n - 2).fill(b), [a]
//         ].reduce((a, b) => a.concat(b))
//     } else {
//         return Array(n).fill(a)
//     }
// }

// function box(n) {
//     let a = '-'.repeat(n)
//     if (n > 2) {
//         let b = '-' + ' '.repeat(n - 2) + '-'
//         return [a, ...Array(n - 2).fill(b), a]
//     } else {
//         return Array(n).fill(a)
//     }
// }

// function box(n) {
//     let a = '-'.repeat(n)
//     return [a, ...Array(n - 2).fill('-' + ' '.repeat(n - 2) + '-'), a]
// }

// const box = n => ['-'.repeat(n), ...Array(n - 2).fill('-' + ' '.repeat(n - 2) + '-'), '-'.repeat(n)]
// const box = n => [...Array(n)].map((_, i) => "-" + (!i || i == n - 1 ? '-' : ' ').repeat(n - 2) + "-")

const box = n => [a = '-'.repeat(n), ...Array(n-2).fill('-'+' '.repeat(n-2)+'-'), a]


q = box(5) // ["-----", "-   -", "-   -", "-   -", "-----"]);
q
q = box(2) // ["--", "--"]);
q
q = box(4) // ["----", "-  -", "-  -", "----"]);
q
q = box(6) // ["------", "-    -", "-    -", "-    -", "-    -", "------"]);
q
q = box(3) // ["---", "- -", "---"]);
q