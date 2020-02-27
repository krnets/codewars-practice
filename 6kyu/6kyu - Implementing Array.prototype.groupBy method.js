// 6kyu - Implementing Array.prototype.groupBy method

/* Add a groupBy method to Array.prototype so that elements in an array could be grouped by the result of 
evaluating a function on each element.

The method should return an object, in which for each different value returned by the function there is a 
property whose value is the array of elements that return the same value.

If no function is passed, the element itself should be taken.

[1,2,3,2,4,1,5,1,6].groupBy()
{
  1: [1, 1, 1],
  2: [2, 2],
  3: [3],
  4: [4],
  5: [5],
  6: [6]
}

[1,2,3,2,4,1,5,1,6].groupBy(function(val) { return val % 3;} )
{
  0: [3, 6],
  1: [1, 4, 1, 1],
  2: [2, 2, 5]
} */

// Array.prototype.groupBy = function (fn) {
//     let obj = {}
//     this.forEach((val, key) => {
//         if (fn) key = fn(val)
//         else key = val
//         if (obj[key]) obj[key].push(val)
//         else obj[key] = [val]
//     })
//     return obj
// }

// Array.prototype.groupBy = function (fn) {
//     let obj = {}
//     this.forEach(val => {
//         let key = fn ? fn(val) : val;
//         (obj[key] = obj[key] || []).push(val)
//     })
//     return obj
// }

// Array.prototype.groupBy = function (fn) {
//     return this.reduce((obj, val) => {
//         let key = fn ? fn(val) : val;
//         (obj[key] = obj[key] || []).push(val)
//         return obj
//     }, {})
// }

// Array.prototype.groupBy = function (fn) {
//     return this.reduce((obj, v) => {
//         let k = fn ? fn(v) : v;
//         (obj[k] = obj[k] || []).push(v)
//         return obj
//     }, {})
// }

Array.prototype.groupBy = function (fn = x => x) {
    return this.reduce((obj, v) => {
        obj[fn(v)] = (obj[fn(v)] || []).concat(v)
        return obj
    }, {})
}

q = [1, 2, 3, 2, 4, 1, 5, 1, 6].groupBy()
q

q = JSON.stringify([1, 2, 3, 2, 4, 1, 5, 1, 6].groupBy())
q
// '{"1":[1,1,1],"2":[2,2],"3":[3],"4":[4],"5":[5],"6":[6]}'

q = JSON.stringify([1, 2, 3, 2, 4, 1, 5, 1, 6].groupBy(
    function (_) {
        return _ % 3;
    }
))
q
// '{"0":[3,6],"1":[1,4,1,1],"2":[2,2,5]}'

var words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten'];
q = JSON.stringify(words.groupBy(
    function (_) {
        return _.length;
    }
))
q
// '{"3":["one","two","six","ten"],"4":["four","five","nine"],"5":["three","seven","eight"]}'