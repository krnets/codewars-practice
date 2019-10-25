// function extraPerfect(n) {
//     let arr = []
//     for (let i = 1; i <= n; i += 2)
//         arr.push(i)
//     return arr
// }

// const extraPerfect = n => Array.from({length: n}, (_, i) => i + 1).filter(i => i % 2)

const extraPerfect = n => [...Array(n + 1).keys()].filter(cur => cur % 2);

q = extraPerfect(3) // [1,3]);
q
q = extraPerfect(5) // [1,3,5]);
q
q = extraPerfect(7) // [1,3,5,7]);
q
q = extraPerfect(28) //, [1,3,5,7,9,11,13,15,17,19,21,23,25,27]);
q
q = extraPerfect(39) //, [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39]);
q