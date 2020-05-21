// 7kyu - Regexp Basics - is it a letter?

/* Implement String#letter? (Ruby), StringUtils.isLetter(String) (Java), String.prototype.isLetter() (JavaScript) or letter? (Clojure), 
which should return true if given object is a single ASCII letter (lower or upper case), false otherwise.
Fundamentals | Regular Expressions | Declarative Programming | Advanced Language Features | Strings */


String.prototype.isLetter = function () {
    return /^[a-z]$/i.test(this)
}

q = "".isLetter() // false
q
q = "a".isLetter() // true
q
q = "X".isLetter() // true
q
q = "7".isLetter() // false
q
q = "*".isLetter() // false
q
q = "ab".isLetter() // false
q
q = "a\n".isLetter() // false
q