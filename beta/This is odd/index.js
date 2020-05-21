// Beta - This is odd

/* Create a function that checks if a number is odd.

Expect negative and decimal numbers too. Remember... all negative numbers can also be either odd or even.

Decimal numbers always return false */


// const isOdd = (n) => Number.isInteger(n) && (n % 2 != 0)

// const isOdd = (n) => Math.abs(n % 2) == 1

const isOdd = (n) => (n + 1) % 2 == 0

q = isOdd(5) // true
q
q = isOdd(4) // false
q
q = isOdd(3) // true
q
q = isOdd(1) // true
q
q = isOdd(0) // false
q
q = isOdd(-5) // true
q
q = isOdd(-4) // false
q
q = isOdd(3.0) // true
q
q = isOdd(-0.1) // false
q
q = isOdd(0.25) // false
q