// 7kyu - Count the divisors of a number

/* Count the number of divisors of a positive integer n.

Random tests go up to n = 500000.

divisors(4)  = 3  // 1, 2, 4
divisors(5)  = 2  // 1, 5
divisors(12) = 6  // 1, 2, 3, 4, 6, 12
divisors(30) = 8  // 1, 2, 3, 5, 6, 10, 15, 30 */

function getDivisorsCnt(n) {
    for (var count = 1, i = 1; i <= n / 2; i++)
        if (n % i == 0) count++
    return count
}

q = getDivisorsCnt(4) // 3  : 1, 2, 4
q
q = getDivisorsCnt(5) // 2  : 1, 5
q
q = getDivisorsCnt(12) // 6  : 1, 2, 3, 4, 6, 12
q
q = getDivisorsCnt(30) // 8  : 1, 2, 3, 5, 6, 10, 15, 30 
q
q = getDivisorsCnt(1) // 1
q
q = getDivisorsCnt(10) // 4
q
q = getDivisorsCnt(11) // 2
q
q = getDivisorsCnt(54) // 8
q