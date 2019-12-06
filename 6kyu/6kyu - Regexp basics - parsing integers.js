// 6kyu - Regexp basics - parsing integers

/* Implement String#to_integer, which should return Integer if object is in one of formats specified below, or nil otherwise:

    Optional - or +
    Base prefix 0b (binary), 0x (hexadecimal), 0o (octal), or in case of no prefix decimal.
    Digits depending on base

Any extra characters, including whitespace, make number invalid, in which case you should return nil.
Digits are case insensitive, but base prefix must be lower case.

Fundamentals | Regular Expressions | Declarative Programming | Advanced Language Features | Strings */

// String.prototype.toInteger = function () {
//     return /(?:^|^-)(0x[0-9a-fA-F]+$)|(0b[01]+$)|(0o[0-7]+$)|(^[-+]?\d+$)/.test(this) ?
//         /^0b/.test(this)  ?  parseInt(this.slice(2), 2) :
//         /^-0b/.test(this) ? -parseInt(this.slice(3), 2) :
//         /^0o/.test(this)  ?  parseInt(this.slice(2), 8) :
//         /^-0o/.test(this) ? -parseInt(this.slice(3), 8) :
//         parseInt(this) : null
// }

// String.prototype.toInteger = function () {
//     return /^[+-]?\d+$/.test(this)             ? parseInt(this) :
//            /^[+-]?0x[\dA-Fa-f]+$/.test(this)   ? parseInt(this, 16) :
//            /^[+-]?0o[0-7]+$/.test(this)        ? parseInt(this.replace(/0o/, ""), 8) :
//            /^[+-]?0b[01]+$|^\d+0b$/.test(this) ? parseInt(this.replace(/0b/, ""), 2) : null
// }

String.prototype.toInteger = function () {
    let match = this.match(/^([+-])?(0b[01]+|0o[0-7]+|0x[\da-fA-F]+|\d+)$/)
    return match ? +((match[1] || '') + +match[2]) : null
}

q = "-0b1010".toInteger() // -0b1010
q
q = "123".toInteger() // 123
q
q = "0x123".toInteger() // 0x123
q
q = "0o123".toInteger() // 0o123
q
q = "0123".toInteger() // 123
q
q = "0b1010".toInteger() // 0b1010
q
q = "+123".toInteger() // 123
q
q = "-123".toInteger() // -123
q
q = "-0x123".toInteger() // -0x123
q
q = "-0o123".toInteger() // -0123
q
q = "-0123".toInteger() // -123
q
q = "0xDEADbeef".toInteger() // 0xDEADBEEF
q
q = "0X123".toInteger() // null
q
q = "0O123".toInteger() // null
q
q = "0B1010".toInteger() // null
q
q = "0b12".toInteger() // null
q
q = "0o18".toInteger() // null
q
q = "123\n".toInteger() // null
q
q = "\n123".toInteger() // null
q
q = "123 ".toInteger() // null
q
q = " 123".toInteger() // null
q