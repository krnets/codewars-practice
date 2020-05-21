// 6kyu - Make the Deadfish swim

/* Write a simple parser that will parse and run Deadfish.

Deadfish has 4 commands, each 1 character long:

    i increments the value (initially 0)
    d decrements the value
    s squares the value
    o outputs the value into the return array

Invalid characters should be ignored. */

// function parse(data) {
//     let res = []
//     for (let val = 0, i = 0; i < data.length; i++) {
//         switch (data[i]) {
//             case 'i':
//                 val++
//                 break
//             case 'd':
//                 val--
//                 break
//             case 's':
//                 val *= val
//                 break
//             case 'o':
//                 res.push(val)
//                 break
//         }
//     }
//     return res
// }

// function parse(data) {
//     let val = 0
//     let res = []
//     for (let command of data) {
//         switch (command) {
//             case 'i':
//                 val++
//                 break
//             case 'd':
//                 val--
//                 break
//             case 's':
//                 val *= val
//                 break
//             case 'o':
//                 res.push(val)
//                 break
//         }
//     }
//     return res
// }

// function parse(data) {
//     let res = [];
//     [...data].reduce((val, c) => {
//         if (c == 'i') val++
//         if (c == 'd') val--
//         if (c == 's') val *= val
//         if (c == 'o') res.push(val)
//         return val
//     }, 0)
//     return res
// }


const parse = data => [...data].reduce(({ val, output }, op) => {
    if (op == 'i') val++
    if (op == 'd') val--
    if (op == 's') val *= val
    if (op == 'o') output.push(val)
    return { val, output } }, { val: 0, output: [] }).output

q = parse("iiisdoso") // [ 8, 64 ] 
q
q = parse("iiisxxxdoso") // [ 8, 64 ] 
q