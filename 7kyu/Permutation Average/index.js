// 7kyu - Permutation Average

/* A number is simply made up of digits.
The number 1256 is made up of the digits 1, 2, 5, and 6.
For 1256 there are 24 distinct permutations of the digits:
1256, 1265, 1625, 1652, 1562, 1526, 2156, 2165, 2615, 2651, 2561, 2516,
5126, 5162, 5216, 5261, 5621, 5612, 6125, 6152, 6251, 6215, 6521, 6512.

Your goal is to write a program that takes a number, n, and returns the average value of all distinct permutations of the digits in n. Your answer should be rounded to the nearest integer. For the example above the return value would be 3889. *

n will never be negative

A few examples:

permutation_average(2)
return 2

permutation_average(25)
>>> 25 + 52 = 77
>>> 77 / 2 = 38.5
return 39 *

permutation_average(20)
>>> 20 + 02 = 22
>>> 22 / 2 = 11
return 11

permutation_average(737)
>>> 737 + 377 + 773 = 1887
>>> 1887 / 3 = 629
return 629

Note: Your program should be able to handle numbers up to 6 digits long */

// function permutations(str) {
//     return str.length <= 1 ? [str] :
//         Array.from(new Set(
//             str.split('')
//             .map((char, i) => permutations(str.substr(0, i) + str.substr(i + 1)).map(p => char + p))
//             .reduce((r, x) => r.concat(x), [])
//         ))
// }
// let aa = permutations(String(n))
// return Math.round(aa.reduce((a,b) => a + Number(b),0) / aa.length)

// function permutationAverage(n) {
//     let rotate = (s, i) => s.slice(i) + s.slice(0, i)
//     let numstr = String(n)
//     let permutations = Array(numstr.length).fill().map((_, i) => rotate(numstr, i))
//     return Math.round(permutations.reduce((a, b) => a + Number(b), 0) / numstr.length)
// }

function permutationAverage(n) {
    let sum = 0
    let numstr = String(n)
    for (let i = 0; i < numstr.length; i++) {
        sum += Number(numstr)
        numstr = numstr.slice(-1) + numstr.slice(0, numstr.length - 1)
    }
    return Math.round(sum / numstr.length)
}

q = permutationAverage(2) // 2
q
q = permutationAverage(25) // 39
q
q = permutationAverage(737) // 629
q
q = permutationAverage(1397) // 5555
q
q = permutationAverage(76853) // 64444
q