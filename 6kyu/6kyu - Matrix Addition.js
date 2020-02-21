// 6kyu - Matrix Addition

/* Write a function that accepts two square matrices (N x N two dimensional arrays), and return the sum of the two. 
Both matrices being passed into the function will be of size N x N (square), containing only integers.

How to sum two matrices:

Take each cell [n][m] from the first matrix, and add it with the same [n][m] cell from the second matrix. 
This will be cell [n][m] of the solution matrix.

Visualization:

|1 2 3|     |2 2 1|     |1+2 2+2 3+1|     |3 4 4|
|3 2 1|  +  |3 2 3|  =  |3+3 2+2 1+3|  =  |6 4 4|
|1 1 1|     |1 1 3|     |1+1 1+1 1+3|     |2 2 4|

 matrixAddition(
  [ [1, 2, 3],
    [3, 2, 1],
    [1, 1, 1] ],
       +
  [ [2, 2, 1],
    [3, 2, 3],
    [1, 1, 3] ] ))

 returns:
  [ [3, 4, 4],
    [6, 4, 4],
    [2, 2, 4] ]

 */

// function matrixAddition(a, b) {
//     let res = []
//     for (let row = 0; row < a.length; row++) {
//         let inner = []
//         for (let col = 0; col < a.length; col++) {
//             inner.push(a[row][col] + b[row][col])
//         }
//         res.push(inner)
//     }
//     return res
// }

// function matrixAddition(a, b) {
//     let matrix = a.slice()
//     for (let row = 0; row < a.length; row++)
//         for (let col = 0; col < a.length; col++)
//             matrix[row][col] = a[row][col] + b[row][col]
//     return matrix
// }

const matrixAddition = (a, b) => a.map((row, i) => row.map((col, j) => col + b[i][j]))

q  = matrixAddition( [ [1, 2], [1, 2] ],  [ [2, 3], [2, 3] ] ) //    = [ [3, 5], [3, 5] ] 
q
q  = matrixAddition( [ [1] ], [ [2] ] ) //   = [ [3] ]
q
q  = matrixAddition( [ [1, 2, 3], [3, 2, 1], [1, 1, 1] ], [ [2, 2, 1], [3, 2, 3], [1, 1, 3] ] ) 
// [ [3, 4, 4], [6, 4, 4], [2, 2, 4] ] )
q