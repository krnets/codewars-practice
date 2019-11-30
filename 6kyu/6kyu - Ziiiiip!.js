// 6kyu - Ziiiiip!

/* Let's implement the zipObject function that enables such results

zipObject(['fred', 'barney'], [30, 40]) => { 'fred': 30, 'barney': 40 }
zipObject([['fred', 30], ['barney', 40]]) => { 'fred': 30, 'barney': 40 }

The zipObject creates an object composed from arrays of keys and values. 
It is provided with either a single two dimensional array, i.e. 
[[key1, value1], [key2, value2]] or with two arrays, one of keys and one of corresponding values.

If only keys are given, then set the values to undefined.

zipObject(['fred', 'barney']) => { fred: undefined, barney: undefined }

If neither keys nor values are specified, then return {}

zipObject() => {} */

// function zipObject(keys, values) {
//     let obj = {}
//     if (!keys && !values) return {}
//     if (typeof keys[0] == 'object') {
//         keys = keys.reduce((a, b) => a.concat(b), [])
//         for (let i = 0; i < keys.length; i += 2)
//             obj[keys[i]] = keys[i + 1]
//     } else if (arguments.length == 2) {
//         for (let i = 0; i < keys.length; i++)
//             obj[keys[i]] = values[i]
//     } else {
//         for (let i = 0; i < keys.length; i++)
//             obj[keys[i]] = undefined
//     }
//     return obj
// }

// function zipObject(keys, values) {
//     var result = {};
//     (keys || []).forEach(function (item, index) {
//         if (item instanceof Array)
//             result[item[0]] = item[1]
//         else
//             result[item] = (values || [])[index]
//     })
//     return result
// }

// const zipObject = (keys = [], values = []) => {
//     return keys.reduce((obj, keypair, i) => {
//         (Array.isArray(keypair)) ? obj[keypair[0]] = keypair[1]: obj[keypair] = values[i]
//         return obj 
//     }, {})
// }

const zip = (arr1 = [], arr2 = []) => arr1.reduce((obj, v, i) => (obj[v] = arr2[i], obj), {}),
    isNested = (arr = []) => Array.isArray(arr[0]),
    split = (arr = []) => arr.reduce((ar, [k, v]) => [ [...ar[0], k], [...ar[1], v] ], [ [], [] ]),
    zipObject = (keys, values) => isNested(keys) ? zip(...split(keys)) : zip(keys, values);

// const zipObject = (keys = [], values) => keys
//     .map((k, i) => Array.isArray(k) ? k : [k, (values || [])[i]])
//     .reduce((a, [k, v]) => (a[k] = v, a), {})

q = zipObject(['fred', 'barney'], [30, 40]) // { 'fred': 30, 'barney': 40 }
q
q = zipObject([ ['fred', 30], ['barney', 40] ]) // { 'fred': 30, 'barney': 40 }
q
q = zipObject() // {}
q
q = zipObject(['fred', 'barney']) // { 'fred': undefined, 'barney': undefined }
q