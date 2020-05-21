// 7kyu - Find the next perfect square!

/* You might know some pretty large perfect squares. But what about the NEXT one?

Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter. 
Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.

If the parameter is itself not a perfect square, than -1 should be returned. You may assume the parameter is positive.

findNextSquare(121) --> returns 144
findNextSquare(625) --> returns 676
findNextSquare(114) --> returns -1 since 114 is not a perfect

Fundamentals | Numbers | Algebra | Mathematics | Algorithms */

// const findNextSquare = (sq) => Number.isInteger(Math.sqrt(sq)) ? Math.pow(Math.sqrt(sq) + 1, 2) : -1
const findNextSquare = (sq) => Math.sqrt(sq) % 1 ? -1 : Math.pow(Math.sqrt(sq) + 1, 2)

q = findNextSquare(121) // 144
q
q = findNextSquare(625) // 676
q
q = findNextSquare(319225) // 320356
q
q = findNextSquare(15241383936) // 15241630849
q
q = findNextSquare(155) // -1
q
q = findNextSquare(342786627) // -1
q