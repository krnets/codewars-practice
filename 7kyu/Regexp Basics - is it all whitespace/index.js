// 7kyu - Regexp Basics - is it all whitespace?

/* Implement String#whitespace?(str) (Ruby), String.prototype.whitespace(str) (JavaScript), String::whitespace(str) (CoffeeScript), 
or whitespace(str) (Python), which should return true/True if given object consists exclusively of zero or more whitespace characters, 
false/False otherwise.

Fundamentals | Regular Expressions | Declarative Programming | Advanced Language Features | Strings | Parsing | Algorithms */

String.prototype.whitespace = function () {
    return /^\s*$/.test(this)
}

q = "".whitespace() // true
q
q = " ".whitespace() // true
q
q = "\n\r\n\r".whitespace() // true
q
q = "a".whitespace() // false
q
q = "w\n".whitespace() //false
q
q = "\t".whitespace() // true
q
q = " a\n".whitespace() // false
q
q = "\t \n\r\n  ".whitespace() // true
q
q = "\n\r\n\r ".whitespace() // true
q
q = "\n\r\n\r 3".whitespace() // false
q