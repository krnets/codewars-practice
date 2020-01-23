// 7kyu - The old switcheroo 2

/* Write function encode(str)
that takes in a string str and replaces all the letters with their respective positions in the English alphabet.

encode('abc') == '123'   // a is 1st in English alpabet, b is 2nd and c is 3rd
encode('codewars') == '315452311819'
encode('abc-#@5') == '123-#@5'

String are case sensitive.
Bonus point if you don't use toLowerCase() */

// const encode = (str) => str.replace(/[a-z]/gi, c => c.toUpperCase().charCodeAt() - 64)
// const encode = (str) => str.replace(/[a-z]/gi, c => c.charCodeAt() - (c < "a" ? 64 : 96))
// const encode = (str) => str.replace(/[a-z]/gi, c => c.charCodeAt() & 31)
const encode = (str) => str.replace(/[a-z]/gi, c => c.charCodeAt() % 32)

q = encode('abc') // '123'
q
q = encode('ABCD') // '1234'
q
q = encode('ZzzzZ') // '2626262626'
q
q = encode('abc-#@5') // '123-#@5'
q