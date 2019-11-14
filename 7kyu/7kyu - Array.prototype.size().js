// 7kyu - Array.prototype.size()

Array.prototype.size = function () {
    let count = 0
    this.forEach(() => count++)
    return count
}

// Object.defineProperty(Array.prototype, 'size', {
//     value() {
//         const last = this.slice(-1)[0];
//         return this.lastIndexOf(last) + 1;
//     }
// })

// Array.prototype.size = function () {
//     return this.reduce(acc => acc + 1, 0)
// }

// Array.prototype.size = function () {
//     return this[0] === undefined ? 0 : 1 + this.slice(1).size()
// }

// Array.prototype.size = function () {
//     return this.unshift();
// }

q = [1].size() // 1
q
q = [1, 2].size() // 2
q
q = [1, 1].size() // 2
q
q = [e, i, pi, 1, 0].size() // 5
q
q = [false, true].size() // 2
q
q = [true, false].size() // 2
q
q = [null].size() // 1
q