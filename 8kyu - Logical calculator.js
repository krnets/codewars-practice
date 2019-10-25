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