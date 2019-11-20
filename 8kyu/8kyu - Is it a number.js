// 8kyu - Is it a number?

// Given a string s, write a method (function) that will return 
// true if its a valid single integer or floating number or false if its not.

// const isDigit = s => s == parseFloat(s)
// const isDigit = s => !!s.trim() && !isNaN(s)
// const isDigit = s => parseFloat(s) == Number(s)
// const isDigit = s => /^-?\d+(\.\d+)?$/.test(s)


q = isDigit("s2324") // false
q
q = isDigit("-234.4") // true
q
q = isDigit("3") // true
q
q = isDigit("  3  ") // true
q
q = isDigit("-3.23") // true
q
q = isDigit("3-4") // false
q
q = isDigit("  3   5") // false
q
q = isDigit("3 5") // false
q
q = isDigit("zero") // false
q