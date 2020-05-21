// 6kyu - Simple Fun #231: Kth Divisor

/* Given integers n and k, find the kth divisor (1-based) of n or determine if n has less than k divisors(return -1).

[input] integer n
5 ≤ n ≤ 10^8.

[input] integer k
1 ≤ k ≤ 20.

[output] an integer
The kth divisor of n or -1 if n has less than k divisors.

For n = 63 and k = 4, the output should be 9.
Divisors of number 63 are the following: 1, 3, 7, 9, 21, 63.

For n = 5 and k = 3, the output should be -1.
Number 5 has only 2 divisors. */

// function kthDivisor(n, k) {
//     let divisors = []
//     for (let i = 1; i <= Math.sqrt(n); i++)
//         if (n % i == 0) {
//             divisors.push(i)
//             if (i != Math.sqrt(n)) {
//                 divisors.push(n / i)
//             }
//         }
//     if (!divisors.includes(n)) {
//         divisors.push(n)
//     }
//     return divisors.sort((a, b) => a - b)[k - 1] || -1
// }

function kthDivisor(n, k) {
    let divisors = []
    for (let i = 1; i <= Math.sqrt(n); i++) {
        if (n % i == 0) {
            divisors.push(i)
            if (i != Math.sqrt(n)) divisors.push(n / i)
        }
    }
    divisors.sort((a, b) => a - b)
    return divisors[k - 1] || -1
}

q = kthDivisor(63, 4) // 9
q
q = kthDivisor(5, 3) // -1
q
q = kthDivisor(100, 10) // -1
q
q = kthDivisor(16, 5) // 16
q
q = kthDivisor(239, 3) // -1
q