// 7kyu - How many twos?

/* Write a function that returns the number of '2's in the factorization of a number.
For example,

twoCount(24)

should return 3, since the factorization of 24 is 2^3 x 3

twoCount(17280)

should return 7, since the factorization of 17280 is 2^7 x 5 x 3^3
The number passed to two_count (twoCount) will always be a positive integer greater than or equal to 1. */

const twoCount = (n) => n.toString(2).match(/0*$/g)[0].length

// const twoCount = (n) => n % 2 == 0 ? 1 + twoCount(n / 2) : 0

q = twoCount(24) // 3
q
q = twoCount(17280) // 7
q
q = twoCount(222222222222) // 1
q
q = twoCount(256) // 8
q
q = twoCount(1) // 0
q
q = twoCount(2) // 1
q
q = twoCount(256) // 8
q
q = twoCount(7) // 0
q
q = twoCount(84934656) // 20
q