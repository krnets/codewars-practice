// 6kyu - Multiplication Tables

/* Create a function that accepts dimensions, of Rows x Columns, as parameters in order 
to create a multiplication table sized according to the given dimensions. 
**The return value of the function must be an array, and the numbers must be Fixnums, NOT strings.

multiplication_table(3,3)

1 2 3
2 4 6
3 6 9

-->[[1,2,3],[2,4,6],[3,6,9]]

Each value on the table should be equal to the value of multiplying the number in its first row times the number in its first column.
Fundamentals | Mathematics | Algorithms | Numbers */

const multiplicationTable = (row, col) => Array(row).fill().map((_, i) => Array(col).fill(i + 1).map((x, idx) => x + idx * x))
// const multiplicationTable = (row, col) => Array(row).fill().map((_, i) => Array(col).fill(i + 1).map((_, j) => (i + 1) * (j + 1)))
// const multiplicationTable = (row, col) => Array(...Array(row)).map((_, i) => Array(...Array(col)).map((_, j) => (i + 1) * (j + 1)))
// const multiplicationTable = (row, col) => [...Array(row)].map((_, i) => [...Array(col)].map((_, j) => (i + 1) * (j + 1)))
// function multiplicationTable(row, col) {
//     let table = []
//     for (let i = 1; i < row + 1; i++) {
//         let inner = []
//         for (let j = 1; j < col + 1; j++) inner.push(i * j)
//         table.push(inner)
//     }
//     return table
// }

q = multiplicationTable(2, 2) // [[1,2],[2,4]]
q
q = multiplicationTable(3, 3) // [[1,2,3],[2,4,6],[3,6,9]]
q
q = multiplicationTable(3, 4) // [[1,2,3,4],[2,4,6,8],[3,6,9,12]]
q
q = multiplicationTable(4, 4) // [[1,2,3,4],[2,4,6,8],[3,6,9,12],[4,8,12,16]]
q
q = multiplicationTable(2, 5) // [[1,2,3,4,5],[2,4,6,8,10]]
q