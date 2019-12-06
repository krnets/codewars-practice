// 7kyu - Regexp Basics - is it a hexadecimal number?

String.prototype.hexNumber = function () {
    return /^(0x)?[0-9A-F]+$/i.test(this)
}

q = ''.hexNumber() // false
q
q = '0x'.hexNumber() // false
q
q = '0'.hexNumber() // true
q
q = '0xDEADBEEF'.hexNumber() // true
q
q = '1337bAbe'.hexNumber() // true
q