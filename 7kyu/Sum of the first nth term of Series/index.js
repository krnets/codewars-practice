// 7kyu - Sum of the first nth term of Series

/* Your task is to write a function which returns the sum of following series upto nth term(parameter).

Series: 1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16 +...

    You need to round the answer to 2 decimal places and return it as String.
    If the given value is 0 then it should return 0.00
    You will only be given Natural Numbers as arguments.

SeriesSum(1) => 1 = "1.00"
SeriesSum(2) => 1 + 1/4 = "1.25"
SeriesSum(5) => 1 + 1/4 + 1/7 + 1/10 + 1/13 = "1.57" */

// function SeriesSum(n) {
//     let arr = []
//     for (let i = 1; arr.length != n; i += 3)
//         arr.push(1 / i)
//     return arr.reduce((a, b) => a + b, 0).toFixed(2)
// }

// function SeriesSum(n) {
//     let sum = 0
//     for (let i = 0; i < n; i++)
//         sum += (1 / (3 * i + 1))
//     return sum.toFixed(2)
// }

// const SeriesSum = (n) => Array(n).fill().map((_, i) => 1 / (i * 3 + 1)).reduce((a, b) => a + b, 0).toFixed(2)

const SeriesSum = (n, sum = 0) => n ? SeriesSum(n - 1, sum + 1 / (3 * n - 2)) : sum.toFixed(2)


q = SeriesSum(1) // "1.00"
q
q = SeriesSum(2) // "1.25"
q
q = SeriesSum(3) // "1.39"
q
q = SeriesSum(4) // "1.49"
q