// 7kyu - Regexp Basics - is it a eight bit signed number?

// String.prototype.signedEightBitNumber = function () {
//     return /^(-(1(2[0-8]|[01][0-9])|[1-9][0-9]?)|(1(2[0-7]|[01][0-9])|[1-9]?[0-9]))$/.test(this)
// }

// String.prototype.signedEightBitNumber = function () {
//     return ((Number(this) + 384) % 256 - 128).toString() == this;
// }

String.prototype.signedEightBitNumber = function () {
    return /^(-?([1-9]\d?|1[01]\d|12[0-7])|-128|0)$/.test(this)
}

q = "".signedEightBitNumber() // false
q
q = "0".signedEightBitNumber() // true
q
q = "00".signedEightBitNumber() // false
q
q = "-0".signedEightBitNumber() // false
q
q = "55".signedEightBitNumber() // true
q
q = "-23".signedEightBitNumber() // true
q
q = "042".signedEightBitNumber() // false
q
q = "127".signedEightBitNumber() // true
q
q = "128".signedEightBitNumber() // false
q
q = "-128".signedEightBitNumber() // true
q
q = "-129".signedEightBitNumber() // false
q
q = "999".signedEightBitNumber() // false
q
q = "-999".signedEightBitNumber() // false
q
q = "1\n".signedEightBitNumber() // false
q
q = "1 ".signedEightBitNumber() // false
q
q = " 1".signedEightBitNumber() // false
q
q = "1\n2".signedEightBitNumber() // false
q
q = "+1".signedEightBitNumber() // false
q
q = "--1".signedEightBitNumber() // false
q