// 7kyu - String to integer conversion

/* JavaScript provides a built-in parseInt method.

It can be used like this:

    parseInt("10") returns 10
    parseInt("10 apples") also returns 10

We would like it to return "NaN" (as a string) for the second case because the input string is not a valid number.

You are asked to write a myParseInt method with the following rules:

    It should make the conversion if the given string only contains a single integer value (and eventually spaces - including tabs, line feeds... - at both ends)
    For all other strings (including the ones representing float values), it should return NaN
    It should assume that all numbers are not signed and written in base 10 */

// const myParseInt = str => /^\s*\d+\s*$/.test(str) ? +str : Number.NaN

const myParseInt = str => Number(str.trim() + '.')

q = myParseInt('1') // 1
q
q = myParseInt('  1 ') // 1
q
q = myParseInt('08') // 8
q
q = myParseInt('5 friends')
q
q = isNaN(myParseInt('5 friends'))
q
q = isNaN(myParseInt('16.5'))
q
