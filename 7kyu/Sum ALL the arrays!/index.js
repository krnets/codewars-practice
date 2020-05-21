// 7kyu - Sum ALL the arrays!

// const arraySum = arr => JSON.stringify(arr).match(/[0-9\.]+/g).reduce((a, b) => a + Number(b), 0)

// const arraySum = arr => String(arr).split(',').filter(v => !Number.isNaN(+v)).reduce((a, b) => a + Number(b), 0)
// const arraySum = arr => String(arr).split(',').reduce((a, b) => a + (!Number.isNaN(+b) ? +b : 0), 0)

// const arraySum = arr => arr.reduce((a, b) => a + (Array.isArray(b) ? arraySum(b) : isNaN(b) ? 0 : b), 0)
// const arraySum = arr => arr.reduce((a, b) => Array.isArray(b) ? arraySum(b) + a : isNaN(b) ? a : b + a, 0)

const arraySum = arr => arr.reduce((sum, x) => sum + (Array.isArray(x) ? arraySum(x) : Number(x) || 0), 0)
// const arraySum = arr => arr.reduce((acc, v) => acc + (Array.isArray(v) ? arraySum(v) : Number(v) || 0), 0)

// function arraySum(arr) {
//     return flattenDeep(arr).filter(a=>!isNaN(a)).reduce((s, a) => s + a, 0)
// }

// function flattenDeep(arr1) {
//     return arr1.reduce((acc, val) => Array.isArray(val) ? acc.concat(flattenDeep(val)) : acc.concat(val), []);
// }

// const arraySum = arr => flattenDeep(arr).filter(a => !isNaN(a)).reduce((s, a) => s + a, 0)

// const flattenDeep = arr => arr.reduce((acc, val) => Array.isArray(val) ? acc.concat(flattenDeep(val)) : acc.concat(val), [])

// const arraySum = arr => flattenDeep(arr).reduce((s, a) => s + (Number(a) || 0), 0)


q = arraySum([1, 2]) // 3
q
q = arraySum([1, 2, 3]) // 6
q
q = arraySum([1, 2, [1, 2]]) // 6
q