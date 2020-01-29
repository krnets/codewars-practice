// 7kyu - Thinking & Testing : True or False

/* No Story
No Description
Only by Thinking and Testing
Look at result of testcase, guess the code! */

const testit = (n) => n.toString(2).replace(/0/g, '').length

q = testit(0) // 0
q
q = testit(1) // 1
q
q = testit(2) // 1
q
q = testit(3) // 2
q
q = testit(4) // 1
q
q = testit(5) // 2
q
q = testit(6) // 2
q
q = testit(7) // 3
q
q = testit(8) // 1
q
q = testit(9) // 2
q
q = testit(10) // 2
q
q = testit(100) // 3
q
q = testit(1000) // 6
q
q = testit(10000) // 5
q