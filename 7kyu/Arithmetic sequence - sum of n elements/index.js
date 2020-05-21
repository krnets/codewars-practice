// 7kyu - Arithmetic sequence - sum of n elements

/* ArithmeticSequenceSum(a, r, n), should return the sum of the first (n) elements of a sequence 
in which each element is the sum of the given integer (a), and a number of occurences of the given integer (r), 
based on the element's position within the sequence.

ArithmeticSequenceSum(2, 3, 5) should return 40:
1     2        3          4            5        .... 20
a + (a+r) + (a+r+r) + (a+r+r+r) + (a+r+r+r+r) 
2 + (2+3) + (2+3+3) + (2+3+3+3) + (2+3+3+3+3) = 40


ArithmeticSequenceSum(3, 2, 20) should return  440:
1     2        3          4            5        .... 20
a + (a+r) + (a+r+r) + (a+r+r+r) + (a+r+r+r+r) 
3 + (3+2) + (3+2+2) + (3+2+2+2) + (3+2+2+2+2) = 440 

Fundamentals | Sequences | Arrays */

// const ArithmeticSequenceSum = (a, r, n) => [...Array(n).fill(r).map((v, i) => v * i + a)].reduce((a, b) => a + b)
const ArithmeticSequenceSum = (a, r, n) => [...Array(n)].reduce((sum, _, i) => sum + a + r * i, 0)
// const ArithmeticSequenceSum = (a, r, n) => (n / 2) * (2 * a + (n - 1) * r)
// const ArithmeticSequenceSum = (a, r, n) => a * n + r * n * (n - 1) / 2

q = ArithmeticSequenceSum(3, 2, 20) // 440
q
q = ArithmeticSequenceSum(2, 2, 10) // 110
q
q = ArithmeticSequenceSum(1, -2, 10) // -80
q