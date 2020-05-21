// 7kyu - Regexp basics - parsing prices

/* Implement String#to_cents, which should parse prices expressed as $1.23 and return number of cents, 
or in case of bad format return nil.

Fundamentals | Regular Expressions | Declarative Programming | Advanced Language Features | Strings */

// String.prototype.toCents = function () {
//     if (!/^\$\d+\.\d{1,2}$/.test(this)) return null
//     return Math.round(parseFloat(this.slice(1)) * 100)
// }

String.prototype.toCents = function () {
    return (/^\$\d+\.\d{2}$/.test(this)) ? Math.round(parseFloat(this.slice(1)) * 100) : null
}

// String.prototype.toCents = function () {
//     let m = this.match(/^\$(\d+\.\d{1,2})$/)
//     return m ? Math.round(m[1] * 100) : null
// }

q = "".toCents() // null
q
q = "1".toCents() // null
q
q = "1.23".toCents() // null
q
q = "$1".toCents() // null
q
q = "$1.23".toCents() // 123
q
q = "$99.99".toCents() // 9999
q
q = "$12345678.90".toCents() // 1234567890
q
q = "$9.69".toCents() // 969
q
q = "$9.70".toCents() // 970
q
q = "$9.71".toCents() // 971
q
q = "$1.23\n".toCents() // null
q
q = "\n$1.23".toCents() // null
q
q = "$0.69".toCents() // 69
q
q = "$9.69$4.3.7".toCents() // null
q
q = "$9.692".toCents() // null
q