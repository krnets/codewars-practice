// 7kyu - Alternate case

// Write function alternateCase which switch every letter in string from upper to lower and from lower to upper.

const alternateCase = s => s.replace(/\w/g, c => (c == c.toLowerCase() ? c.toUpperCase() : c.toLowerCase()))

q = alternateCase('abc') // "ABC"
q
q = alternateCase('ABC') // "abc"
q
q = alternateCase('Hello World') // "hELLO wORLD"
q
