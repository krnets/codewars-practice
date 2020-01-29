// 7kyu - Thinking & Testing : Retention and discard

/* No Story
No Description
Only by Thinking and Testing
Look at the results of the testcases, and guess the code! */

const testit = (n) => n > 0 ? [...Array(n + 1).keys()].filter(v => v % v == 0 && v % 2 != 0) : []

q = testit(-1) // []
q
q = testit(0) // []
q
q = testit(1) // [1]
q
q = testit(2) // [1]
q
q = testit(3) // [1,3]
q
q = testit(4) // [1]
q
q = testit(5) // [1,5]
q
q = testit(6) // [1,3]
q
q = testit(7) // [1,7]
q
q = testit(8) // [1]
q
q = testit(9) // [1,3,9]
q
q = testit(10) // [1,5]
q