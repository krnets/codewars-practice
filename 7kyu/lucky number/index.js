// 7kyu - lucky number

/* Write a function to find if a number is lucky or not. 
If the sum of all digits is 0 or multiple of 9 then the number is lucky.

1892376 => 1+8+9+2+3+7+6 = 36. 36 is divisble by 9, hence number is lucky.

Function will return true for lucky numbers and false for others. */

const isLucky = (n) => [...n + ''].reduce((a, b) => a + b * 1, 0) % 9 == 0
// const isLucky = (n) => n % 9 == 0


q = isLucky(1892376) // true, "Wrong result for 1892376"
q
q = isLucky(189237) // false, "Wrong result for 189237"
q
q = isLucky(1098) // true, "Wrong result for 1098"
q
q = isLucky(22869) // true, "Wrong result for 22869"
q
q = isLucky(0) // true, "Wrong result for 0"
q