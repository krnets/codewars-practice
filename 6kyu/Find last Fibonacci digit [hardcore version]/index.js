// 6kyu - Find last Fibonacci digit [hardcore version]

/* Return the last digit of the nth element in the Fibonacci sequence
(starting with 1,1, to be extra clear, not with 0,1 or other numbers).

You will just get much bigger numbers, so good luck bruteforcing your way through it.

Algorithms | Sequences | Arrays | Parsing | Strings */

// function lastFibDigit(n) {
//     n = n % 60;
//     let fib = [0, 1, 1];
//     for (let i = 3; i <= n; i++) {
//         fib[i] = (fib[i - 1] + fib[i - 2]) % 10;
//     }
//     return fib[n];
// }

// const lastFibDigit = index => +("011235831459437077415617853819099875279651673033695493257291" [index % 60]);

const lastFibDigit = index => [0, 1, 1, 2, 3, 5, 8, 3, 1, 4, 5, 9, 4, 3, 7, 0, 7, 7, 4, 1, 5, 6, 1, 7, 8, 5, 3, 8, 1, 9, 0, 9, 9, 8, 7, 5, 2, 7, 9, 6, 5, 1, 6, 7, 3, 0, 3, 3, 6, 9, 5, 4, 9, 3, 2, 5, 7, 2, 9, 1][index % 60]

q = lastFibDigit(1) // 1
q
q = lastFibDigit(2) // 1
q
q = lastFibDigit(3) // 2
q
q = lastFibDigit(21) // 6
q
q = lastFibDigit(302) // 1
q
q = lastFibDigit(1000) // 5
q
q = lastFibDigit(4003) // 7
q
q = lastFibDigit(1000000) // 5
q
q = lastFibDigit(50004) // 8
q
q = lastFibDigit(600005) // 5
q
q = lastFibDigit(7000006) // 3
q
q = lastFibDigit(80000007) // 8
q
q = lastFibDigit(900000008) // 1
q
q = lastFibDigit(1000000009) // 9
q