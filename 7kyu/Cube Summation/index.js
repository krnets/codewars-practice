// 7kyu - Cube Summation

/* Write a function cubeSum(n, m) that will calculate a sum of cubes of numbers in a given range, 
starting from the smaller (but not including it) to the larger (including). 
The first argument is not necessarily the larger number.
If both numbers are the same, then the range is empty and the result should be 0.

cubeSum(2,3); // => 3^3 = 27
cubeSum(3,2); // => 3^3 = 27
cubeSum(0,4); // => 1^3+2^3+3^3+4^3 = 100
cubeSum(17, 14); // => 15^3+16^3+17^3 = 12384
cubeSum(9, 9); // => 0 */

// function cubeSum(n, m) {
//     if (n < m) {
//         return Array(m - n).fill().map((_, i) => Math.pow(i + n + 1, 3)).reduce((a, b) => a + b, 0)
//     } else if (n > m) {
//         return Array(n - m).fill().map((_, i) => Math.pow(i + m + 1, 3)).reduce((a, b) => a + b, 0)
//     } else return 0
// }

function cubeSum(n, m) {
    let min = Math.min(n, m)
    let max = Math.max(n, m)
    return Array(max - min).fill().map((_, i) => Math.pow(i + 1 + min, 3)).reduce((a, b) => a + b, 0)
}

q = cubeSum(0, 5) // 225, "cubeSum(0,5)"
q
q = cubeSum(5, 0) // 225, "cubeSum(5,0)"
q
q = cubeSum(2, 3) // 27, "cubeSum(2,3)"
q
q = cubeSum(97, 4) // 22590909
q
q = cubeSum(71, 30) // 6316911
q
q = cubeSum(20, 20) // 0
q
q = cubeSum(77, 5) //  9017784
q
q = cubeSum(62, 37) // 3320000
q