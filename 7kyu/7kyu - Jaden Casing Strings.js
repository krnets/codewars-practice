// 7kyu - Jaden Casing Strings

// String.prototype.toJadenCase = function (str) {
//     return this.split(' ').map(w => w[0].toUpperCase() + w.slice(1)).join(' ')
// }

String.prototype.toJadenCase = function (str) {
    return this.replace(/(^|\s)[a-z]/g, c => c.toUpperCase())
}

// String.prototype.toJadenCase = function (str) {
//     return this.replace(/(?:^|\s)\S/g, c => c.toUpperCase())
// }

var str = "How can mirrors be real if our eyes aren't real";
q = str.toJadenCase()
q
//  "How Can Mirrors Be Real If Our Eyes Aren't Real"