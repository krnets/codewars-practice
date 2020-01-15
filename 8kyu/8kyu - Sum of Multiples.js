// 8kyu - Sum of Multiples

/* Find the sum of all multiples of n below m

    n and m are natural numbers (positive integers)
    m is excluded from the multiples

sumMul(2, 9)   ==> 2 + 4 + 6 + 8 = 20
sumMul(3, 13)  ==> 3 + 6 + 9 + 12 = 30
sumMul(4, 123) ==> 4 + 8 + 12 + ... = 1860
sumMul(4, -7)  ==> "INVALID" */

function sumMul(n, m) {
    for (var sum = 0, i = n; i < m; i += n)
        sum += i
    return sum > 0 ? sum : 'INVALID'
}

q = sumMul(0, 0) // "INVALID"
q
q = sumMul(2, 9) // 20
q
q = sumMul(4, -7) // "INVALID"
q