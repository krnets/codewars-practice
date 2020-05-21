// 6kyu - Trim a String

/* Define a function trim which removes all forms of leading and trailing whitespace from a given string. Please refer to the Sample Tests for more examples.
Fundamentals | Strings | Regular Expressions | Declarative Programming | Advanced Language Features */

// String.prototype.trim = function () {
//     return this.replace(/^\s+/g, '').replace(/\s+$/g, '')
// }

// String.prototype.trim = function () {
//     return this.replace(/^[\s]+|[\s]+$/g, '')
// }

String.prototype.trim = function () {
    return this.replace(/^\s+|\s+$/g, '')
}

q = "foo      ".trim() // "foo", "trailing spaces"
q
q = "      foo".trim() // "foo", "leading spaces"
q
q = "      foo      ".trim() // "foo", "leading and trailing spaces"
q
q = "foo    bar".trim() // "foo    bar", "spaces in between"
q
q = "    ".trim() // "", "only spaces"
q