// 7kyu - Is It Negative Zero (-0)?

/* There exist two zeroes: +0 (or just 0) and -0.
Write a function that returns true if the input number is -0 and false otherwise (True and False for Python).
In JavaScript / TypeScript / Coffeescript th input will be a number. */

const isNegativeZero = (n) => Object.is(0, -n)

q = isNegativeZero(-0) // true
q
q = isNegativeZero(-Infinity) // false
q
q = isNegativeZero(-5) // false
q
q = isNegativeZero(-4) // false
q
q = isNegativeZero(-3) // false
q
q = isNegativeZero(-2) // false
q
q = isNegativeZero(-1) // false
q
q = isNegativeZero(-Number.MIN_VALUE) // false
q
q = isNegativeZero(0) // false
q
q = isNegativeZero(Number.MIN_VALUE) // false
q
q = isNegativeZero(1) // false
q
q = isNegativeZero(2) // false
q
q = isNegativeZero(3) // false
q
q = isNegativeZero(4) // false
q
q = isNegativeZero(5) // false
q
q = isNegativeZero(Infinity) // false
q
