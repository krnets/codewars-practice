// 7kyu - Rearange Number to Get its Maximum

/* Create function that takes one positive three digit integer and rearranges its digits to get maximum possible number. 
Assume that argument is integer. Return null (nil for ruby) if argument is not valid. */

// const maxRedigit = n => (s = [...String(n)]).length == 3 ? +[...String(n)].sort((a, b) => b - a).join `` : null
const maxRedigit = n => (r = [...String(n)]).length == 3 ? +r.sort((a, b) => b - a).join `` : null

// Basic test
q = maxRedigit(123) // 321, "123 => 321"
q

// Edge cases test
q = maxRedigit(-1) // null, "-1 => null"
q
q = maxRedigit(0) // null, "0 => null"
q