// 8kyu - Type of sum

// Return the type of the sum of the two arguments

// function typeOfSum(a, b) {
//     return typeof a == 'string' && typeof b == 'string'    ? 'string' :
//         typeof a == 'string'    && typeof b == 'number'    ? 'string' :
//         typeof a == 'string'    && typeof b == 'object'    ? 'string' :
//         typeof a == 'string'    && typeof b == 'boolean'   ? 'string' :
//         typeof a == 'string'    && typeof b == 'undefined' ? 'string' :
//         typeof a == 'object'    && typeof b == 'string'    ? 'string' :
//         typeof a == 'number'    && typeof b == 'string'    ? 'string' :
//         typeof a == 'boolean'   && typeof b == 'string'    ? 'string' :
//         typeof a == 'undefined' && typeof b == 'string'    ? 'string' :
//         'number'
// }

const typeOfSum = (a, b) => typeof (a + b)

q = typeOfSum('s', null) // 'string'
q
q = typeOfSum(12, 1) // 'number'
q
q = typeOfSum('d', 1) // 'string'
q
q = typeOfSum(1, 'a') // 'string'
q
q = typeOfSum('dd', '') // 'string'
q
q = typeOfSum(true, 1) // 'number'
q
q = typeOfSum('s', false) // 'string'
q
q = typeOfSum(null, 1) // 'number'
q
q = typeOfSum(null, undefined) // 'number'
q
q = typeOfSum(undefined, 're') // 'string'
q
q = typeOfSum(undefined, true) // 'number'
q
q = typeOfSum(null, false) // 'number'
q