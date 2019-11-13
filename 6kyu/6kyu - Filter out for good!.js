// 6kyu - Filter out for good!

// Array.prototype.remove = function (pred) {
//     let out  = []
//     let keep = []
//     for (let i = 0; i < this.length; i++) {
//         if (pred(this[i]))
//             out.push(this[i])
//         else
//             keep.push(this[i])
//     }
//     this.length = keep.length
//     for (let i = 0; i < keep.length; i++)
//         this[i] = keep[i]
//     return out
// }

// Array.prototype.remove = function (pred) {
//     let arrayCp = this.splice(0, this.length);
//     return arrayCp.filter(function (item) {
//         return pred(item) ? true : !this.push(item);
//     }, this)
// }

// Array.prototype.remove = function (pred) {
//     var removed = []
//     var arr = Object.assign([], this)
//     this.splice(0, this.length)
//     for (var a of arr)
//         if (pred(a)) removed.push(a)
//         else this.push(a)
//     return removed
// }

Array.prototype.remove = function (pred) {
    let out = this.filter(pred)
    let keep = this.filter(v => !pred(v))
    this.splice(0, this.length)
    keep.forEach(v => this.push(v))
    return out
}


var array = [1, 2, 3, 4, 5];
var predicate = i => i % 2 === 0;
var removed = array.remove(predicate);
q = removed // [2,4]
q
q = array // [1, 3, 5]
q

array = [1, 2, 3, 4, 5];
predicate = i => i % 2 !== 0;
removed = array.remove(predicate);
q = removed // [1, 3, 5]
q
q = array // [2, 4]
q

array = [2, 2, 2, 2, 2];
predicate = i => i === 2;
removed = array.remove(predicate);
q = removed // [2, 2, 2, 2, 2]
q
q = array // []
q

array = ['a', 'b', 'c', 'd', 'e'];
predicate = i => i >= 'a' && i <= 'd';
removed = array.remove(predicate);
q = removed // ['a', 'b', 'c', 'd']
q
q = array // ['e']
q