// 8 kyu - Logical calculator

function logicalCalc(array, op) {
    switch (op) {
        case 'AND':
            return array.reduce((accum, val) => accum && val)
        case 'OR':
            return array.reduce((accum, val) => accum || val)
        case 'XOR':
            return array.reduce((accum, val) => accum != val)
    }
}

// function logicalCalc(array, op) {
//     if (op == 'AND') {
//         return array.reduce((accum, val) => accum && val)
//     }
//     if (op == 'OR') {
//         return array.reduce((accum, val) => accum || val)
//     }
//     if (op == 'XOR') {
//         return array.reduce((accum, val) => accum != val)
//     }
// }

// return eval(array.map(x => +x).join({AND: "&", OR: "|", XOR: "^"}[op])) !== 0

// function logicalCalc(array, op) {
//     return eval(array.map(x => +x)
//             .join({
//                 AND: '&',
//                 OR: '|',
//                 XOR: '^'
//             } [op])) !== 0
// }

// const logicalCalc = (array, op) => !!array.reduce(({
//     'A': (a, b) => a & b,
//     'O': (a, b) => a | b,
//     'X': (a, b) => a ^ b
// })[op[0]]);

// const logicalCalc = (array, op) =>
//     op == 'XOR' ? true == ((a,b) => a ^ b) :
//     array[{AND: 'every', OR: 'some'}[op]] (Boolean)  // <-- overly clever

q = logicalCalc([true, true, true, false], "AND") //false);
q
q = logicalCalc([true, true, true, false], "OR") // true);
q
q = logicalCalc([true, true, true, false], "XOR") // true);
q
q = logicalCalc([true, true, false, false], "AND") //false);
q
q = logicalCalc([true, true, false, false], "OR") // true);
q
q = logicalCalc([true, true, false, false], "XOR") //false);
