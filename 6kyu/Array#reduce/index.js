// 6kyu - Array#reduce

// Array.prototype.reduce = function (process, initial) {
//     for (let i = 0; i < this.length; i++) {
//         if (!initial) {
//             initial = this[0]
//             i++
//         }
//         initial = process(initial, this[i])
//     }
//     return initial
// }

Array.prototype.reduce = function (process, initial) {
    let defaults = { 'string': '', 'number': 0 } [typeof (this[0])];
    this.forEach((v, i) => initial = process(initial || defaults, v, i, this));
    return initial;
}

q = ['a', 'y', '!'].reduce(function (x, y) { return x + y }, 'y') // 'yay!'
q
q = ['a', 'y', '!'].reduce(function (x, y) { return x + y } ) // 'yay!'
q