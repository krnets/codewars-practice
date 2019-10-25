// const wordValue = a =>
//     a.map((str, index) => str
//         .split('')
//         .map((v, i) => str.charCodeAt(i) - 96)
//         .filter(v => v > 0)
//         .reduce((a, b) => a + b, 0))
//     .map((v, i) => v * (i + 1))

// const wordValue = a =>
//     a.map((str, index) => str
//         .replace(/\s/,'')
//         .split('')
//         .map((v) => v.charCodeAt() - 96)
//         // .filter(v => v > 0)
//         // .reduce((acc, cur) => (acc += cur), 0) * (index + 1))
//         // .reduce((acc, cur) => (acc + cur), 0) * (index + 1))
//         .reduce((a, b) => (a + b), 0) 
//               * (index + 1))

// const wordValue = a =>
//     a.map((str, index) => str
//         .replace(/\s/g,'')
//         .split('')
//         .map(v => v.charCodeAt() - 96)
//         .reduce((a, b) => (a + b), 0) 
//             * (index + 1))

const wordValue = a =>
    a.map((str, index) => ++index * [...str]
        .map(v => v.charCodeAt() - 96)
        .filter(v => v > 0)
        .reduce((a, b) => (a + b), 0))

// const wordValue = a =>
//     a.map((str, index) => ++index * [...str.replace(/\s/g, '')]
//         .map(v => v.charCodeAt() - 96)
//         .reduce((a, b) => (a + b), 0))

// const wordValue = a => a.map((str, i) => (i + 1) * str.split``
// .reduce((s, n) => s + 1 + 'abcdefghijklmnopqrstuvwxyz'.indexOf(n), 0))

// const wordValue = (arr) =>
//     arr.map((str, i) => [...str]
//        .reduce((acc, cur) =>
//             acc + -~'abcdefghijklmnopqrstuvwxyz'.indexOf(cur), 0) * ++i)

q = wordValue(["codewars", "abc", "xyz"]) // [88,12,225] 
q
q = wordValue(["abc abc", "abc abc", "abc", "abc"]) // [12,24,18,24] 
q
q = wordValue(["abc"]) //,"abc abc","abc","abc"]) // [12,24,18,24] 
q
// q = wordValue(["abc", "abc abc", "abc", "abc"]) // [12,24,18,24] 
// q