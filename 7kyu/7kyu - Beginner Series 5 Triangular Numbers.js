// 7kyu - Beginner Series #5 Triangular Numbers

/* Triangular number is the amount of points that can fill equilateral triangle.

Example: the number 6 is a triangular number because all sides of a triangle has the same amount of points.

Hint!
T(n) = n * (n + 1) / 2,
n - is the size of one side.
T(n) - is the triangular number.

Given a number 'T' from interval [1; 2147483646], find if it is triangular number or not. */

// function isTriangular(t) {
//     for (let n = 1; n <= t; n++)
//         if (n * (n + 1) / 2 == t) return true
//     return false
// }

const isTriangular = (t) => Math.sqrt(8 * t + 1) % 1 == 0

q = isTriangular(1) //  true
q
q = isTriangular(3) //  true
q
q = isTriangular(6) //  true
q
q = isTriangular(10) //  true
q
q = isTriangular(15) //  true
q
q = isTriangular(21) //  true
q
q = isTriangular(28) //  true
q
q = isTriangular(2) //  false
q
q = isTriangular(7) //  false
q
q = isTriangular(14) //  false
q
q = isTriangular(27) //  false
q