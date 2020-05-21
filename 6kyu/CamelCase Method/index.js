// 6kyu - CamelCase Method

// String.prototype.camelCase = function () {
//     return this.slice().split(' ').filter(Boolean).map(v => v[0].toUpperCase() + v.slice(1)).join('')
// }

// String.prototype.camelCase = function () {
//     return this.trim().split(' ').map(v => v.slice(0, 1).toUpperCase() + v.slice(1)).join('')
// }

String.prototype.camelCase = function () {
    return this.trim().replace(/(?:^|\s+)(\w)/g, (_, c) => c.toUpperCase())
}

q = "test case".camelCase() // "TestCase"
q
q = "camel case method".camelCase() // "CamelCaseMethod"
q
q = "say hello ".camelCase() // "SayHello"
q
q = " camel case word".camelCase() // "CamelCaseWord"
q
q = "".camelCase() // ""
q