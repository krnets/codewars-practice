// 6kyu - Extract the IDs from the data set

// Complete the method so that it returns an array of all ID's passed in. 
// The method should be able to handle the case of empty data being passed in.
// Note: The only arrays that need to be traversed are those assigned to the "items" property.


// const isArray = o => Object.prototype.toString.call(o) === '[object Array]'
// const traverse = x => (isArray(x)) ? traverseArray(x) : ((typeof x === 'object') && (x !== null)) && traverseObject(x)
// const traverse = x => (Array.isArray(x)) ? traverseArray(x) : ((typeof x === 'object') && (x !== null)) && traverseObject(x)
// const traverseArray = arr => arr.forEach(x => traverse(x))
// const traverseObject = obj => { for (var key in obj) if (obj.hasOwnProperty(key)) traverse(obj[key]) }

// const _ = require('lodash')
// const traverse = obj => {
//     _.forOwn(obj, (val, key) => {
//       if (_.isArray(val)) {
//         val.forEach(el => {
//           traverse(el);
//         });
//       } else if (_.isObject(val)) {
//         traverse(val);
//       } else {
//         // do something with leaf node
//       }
//     });
//   };

// const traverse = (obj) => {
//     for (let k in obj) {
//         if (obj[k] && typeof obj[k] === 'object') {
//             traverse(obj[k])
//         } else {
//             // Do something with obj[k]
//         }
//     }
// }

// const extractIds = data => {
//     let res = []
//     let a = data.id
//     let b = data.items
//     let c = data.items[0]
//     let d = c.id
//     let e = data.items[1]
//     let f = e.id
//     let g = data.items[1].items
//     let h = g[0]
//     let i = h.id
//     let j = g[1]
//     let k = j.id
//     res.push(a, d, f, i, k)
//     return res
// }

const extractIds = data => [].concat(...Object.keys(data).map(v => v == 'id' ? data[v] : extractIds(data[v])))

// const extractIds = data => [data.id].concat(data.items ? data.items.map(extractIds) : [])
//     .filter(x => x).reduce((a, b) => a.concat(b), [])

var data = { id: 1, items: [{ id: 2 }, { id: 3, items: [{ id: 4 }, { id: 5 }]}] }

q = extractIds(data) // should return [1,2,3,4,5]
q