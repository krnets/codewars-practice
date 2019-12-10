// 6kyu - Multiplication table

/* Your task, is to create NxN multiplication table, of size provided in parameter.

for example, when given size is 3:

1 2 3
2 4 6
3 6 9

for given example, the return value should be: [[1,2,3],[2,4,6],[3,6,9]]

Fundamentals | Arithmetic | Mathematics | Algorithms | Numbers | Arrays */

const multiplicationTable = (size) => Array(size).fill().map((_, i) => Array(size).fill(i + 1).map((v, idx) => v + idx * v))
// const multiplicationTable = (size) => Array(size).fill().map((_, i) => Array(size).fill().map((_, j) => (i + 1) * (j + 1)))

q = multiplicationTable(3)
q