// 7kyu - SevenAte9

/* Write a function that removes every lone 9 that is inbetween 7s.

sevenAte9('79712312') => '7712312'
sevenAte9('79797') => '777'

Input: String Output: String */

const sevenAte9 = (str) => str.replace(/79(?=7)/g, '7')

q = sevenAte9('165561786121789797') // '16556178612178977'
q
q = sevenAte9('797') // '77'
q
q = sevenAte9('7979797') // '7777'
q