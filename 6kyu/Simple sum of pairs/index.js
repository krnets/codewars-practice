// 6kyu - Simple sum of pairs

/* Given an integer n, find two integers a and b such that:

A) a >= 0 and b >= 0
B) a + b = n
C) DigitSum(a) + Digitsum(b) is maximum of all possibilities.  
You will return the digitSum(a) + digitsum(b).

solve(29) = 11. If we take 15 + 14 = 29 and digitSum = 1 + 5 + 1 + 4 = 11. There is no larger outcome.
n will not exceed 10e10. */

function solve(n) {
    let a = '9'.repeat(String(n).length - 1)
    let b = n - a
    return [...a + b].reduce((c, d) => c + Number(d), 0)
}

q = solve(1140) // 33
q
q = solve(18) // 18
q
q = solve(29) // 11
q
q = solve(45) // 18
q
q = solve(7019) // 35
q