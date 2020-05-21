// 7kyu - Only one

/* Given any number of boolean flags function should return true if and only if one of them is true 
while others are false. If function is called without arguments it should return false. */

const onlyOne = (...args) => args.filter(Boolean).length == 1

q = onlyOne() // false
q
q = onlyOne(true, false, false) // true
q
q = onlyOne(true, false, false, true) // false
q
q = onlyOne(false, false, false, false) // false  
q
q = onlyOne(true, false) // true
q