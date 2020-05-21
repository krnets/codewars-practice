// 6kyu - Sequences and Series

/* Have a look at the following numbers:

 n | score
---+-------
 1 |  50
 2 |  150
 3 |  300
 4 |  500
 5 |  750

Can you find a pattern in it? 

 50     50 + 100   50 + 100 + 150    50 + 100 + 150 + 200       50 + 100 + 150 + 200 + 250 
 50     150        300               500                        750
 1      2          3                 4                          5

If so, then write a function getScore(n) which returns the score for any positive number n */

// function getScore(n) {
//     let arr = Array(n).fill().map((_, i) => 50 * (i + 1))
//     return arr.map((_, i) => arr.slice(0, i + 1).reduce((a, b) => a + b, 0))[n - 1]
// }

// const getScore = n => n * (n + 1) * 25

// function getScore(n) {
//     for (var arr = [], i = 0, j = 1; i < n; i++, j += i)
//         arr.push(j)
//     return 50 * ((n - 1) + arr[n - 1]) || 50
// }

function getScore(n) {
    for (var sum = 0, i = 0; i < n; i++)
        sum += i * 50
    return sum + n * 50
}

q = getScore(1) // 50
q
q = getScore(2) // 150
q
q = getScore(3) // 300
q
q = getScore(4) // 500
q
q = getScore(5) // 750
q