// 7kyu - Triangular Treasure

/* Triangular numbers are so called because of the equilateral triangular shape that they occupy when laid out as dots. i.e.

1st (1)   2nd (3)    3rd (6)
*          **        ***
           *         **
                     *

You need to return the nth triangular number. You should return 0 for out of range values */

const triangular = (n) => n > 0 ? n * (n + 1) / 2 : 0

q = triangular(2) // 3 
q
q = triangular(4) // 10 
q
q = triangular(0) // 0
q
q = triangular(2) // 3
q
q = triangular(3) // 6
q
q = triangular(-10) // 0
q