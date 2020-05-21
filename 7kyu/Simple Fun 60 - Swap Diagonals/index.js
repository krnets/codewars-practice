// 7kyu - Simple Fun #60: Swap Diagonals

/* The longest diagonals of a square matrix are defined as follows:

the first longest diagonal goes from the top left corner to the bottom right one;
the second longest diagonal goes from the top right corner to the bottom left one.
Given a square `matrix`, your task is to swap its longest diagonals by exchanging their elements at the corresponding positions.

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]the output should be [[3, 2, 1], [4, 5, 6], [9, 8, 7]]

1 2 3   ->  3 2 1
4 5 6   ->  4 5 6
7 8 9   ->  9 8 7 

43  455 32  103  ->  103 455 32  43
102 988 298 981  ->  102 298 988 981
309 21  53  64   ->  309 53  21  64
2   22  35  291  ->  291 22  35  2

    [input] 2D integer array matrix
    Constraints: 1 ≤ matrix.length ≤ 10, matrix.length = matrix[i].length, 1 ≤ matrix[i][j] ≤ 1000.

    [output] 2D integer array
    Matrix with swapped diagonals. */

// function swapDiagonals(matrix) {
//     for (let i = 0; i < matrix.length; i++) {
//         if (i != matrix.length - 1 / 2) {
//             let left = matrix[i][i]
//             let right = matrix[i][matrix[i].length - i - 1]
//             matrix[i][i] = right
//             matrix[i][matrix[i].length - i - 1] = left
//         }
//     }
//     return matrix
// }

function swapDiagonals(matrix) {
    matrix.forEach((row, i) => [row[i], row[matrix.length-i-1]] = [row[matrix.length-i-1], row[i]])
    return matrix
}

// const swapDiagonals = (matrix) => matrix.map((row, i) => ([row[i], row[matrix.length - i - 1]] = [row[matrix.length - i - 1], row[i]], row));

// function swapDiagonals(matrix) {
//     let len = matrix[0].length;
//     for (let [i, row] of matrix.entries())
//       [row[i], row[len - i - 1]] = [row[len - i - 1], row[i]];
//     return matrix;
//   }

q  = swapDiagonals([[1,2,3],  [4,5,6],  [7,8,9]]) 
// [[3,2,1],  [4,5,6],  [9,8,7]]
q
q  = swapDiagonals([[239]]) // [[239]]
q
q  = swapDiagonals( [[1,10],  [100,1000]]) // [[10,1],  [1000,100]]
q
q  = swapDiagonals([[43,455,32,103],  [102,988,298,981],  [309,21,53,64], [2,22,35,291]]) 
// [[103,455,32,43],  [102,298,988,981],  [309,53,21,64], [291,22,35,2]]
q