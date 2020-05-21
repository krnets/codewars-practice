// 6kyu - Array intersect all

// function intersect(...arr) {
//     let set = [...new Set([].concat(...arr))]
//     let common = []
//     for (let i = 0; i < set.length; i++)
//         if (arr.every(v => v.includes(set[i])))
//             common.push(set[i])
//     return common
// }

// var intersect = function () {
//     if (!arguments.length) return [];
//     var arr = Array.prototype.slice.call(arguments);

//     return arr[0].filter(function(val, index){
//       return arr.every(function(v, i){
//         return v.indexOf(val) !== -1;
//       })    
//     });
//   };

// function intersect() {
//     if (!arguments.length) return [];
//     var arr = Array.prototype.slice.call(arguments);
//     return arr[0].filter(val => arr.every((v, i) => v.indexOf(val) !== -1));
// };

// const {intersection} = require("lodash")
// let intersect = (...xss) => intersection(...xss)

// import { intersection } from "lodash"
// let intersect = (...xss) => intersection(...xss)

// const intersect = require("lodash").intersection

// const intersect = (xs, ys, ...arr) => ys === undefined ? xs : intersect(intersect2(xs, ys), ...arr)
// const intersect2 = (xs, ys) => xs.filter(x => ys.some(y => y === x))

// const intersect = (head, ...tail) => tail.length ? head.filter(val => tail.every(v => v.indexOf(val) !== -1)) : []
// const intersect = (head, ...tail) => head ? head.filter(val => tail.every(v => v.indexOf(val) !== -1)) : []
// const intersect = (head, ...tail) => head ? head.filter(v => tail.every(arr => arr.includes(v))) : []
const intersect = (...arr) => arr.length ? arr.reduce((a, b) => a.filter(v => b.includes(v))) : []

var a = ['dog', 'bar', 'foo', 'chai']
var b = ['foo', 'bar', 'cat', 'chai']
var c = ['gin', 'foo', 'bar', 'chai']
var d = ['foo', 'chai']

q = intersect(a, b, c) // ['bar', 'foo', 'chai']
q
q = intersect(a, b, c, d) // ['foo', 'chai']
q