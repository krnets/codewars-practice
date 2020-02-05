// 7kyu - Minimum to multiple

/* Given two integers a and x, 
return the minimum non-negative number to add to / subtract from a to make it a multiple of x.

minimum(10, 6)  //= 2

10+2 = 12 which is a multiple of 6

Note: 0 is always a multiple of x

Constraints:  1 <= a <= 106,  1 <= x <= 105 */


// function minimum(a, x) {
//     for (let i = 0; i <= x; i++) {
//         if ((a + i) % x == 0) return i;
//         if ((a - i) % x == 0) return i;
//     }
// }

const minimum = (a, x) => Math.min(x - a % x, a % x)

q = minimum(1, 10) // 0
q
q = minimum(1, 1) // 0
q
q = minimum(9, 4) // 1
q
q = minimum(10, 6) // 2
q
q = minimum(60, 45) // 15
q
q = minimum(28, 16) // 4
q
q = minimum(84, 80) //  4
q
q = minimum(129, 49) // 18
q
q = minimum(150, 67) // 16
q
q = minimum(121, 46) // 17
q
q = minimum(83, 81) // 2
q
q = minimum(89, 74) // 15
q
q = minimum(57, 50) // 7
q