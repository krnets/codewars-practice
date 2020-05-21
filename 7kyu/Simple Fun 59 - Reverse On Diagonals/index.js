// 7kyu - Simple Fun #59: Reverse On Diagonals

/* Given a square matrix, your task is to reverse the order of elements on both of its longest diagonals.

The longest diagonals of a square matrix are defined as follows:

    the first longest diagonal goes from the top left corner to the bottom right one;
    the second longest diagonal goes from the top right corner to the bottom left one.

For the matrix

1, 2, 3
4, 5, 6
7, 8, 9

the output should be:

9, 2, 7
4, 5, 6
3, 8, 1

    [input] 2D integer array matrix
    Constraints: 1 ≤ matrix.length ≤ 10, matrix.length = matrix[i].length, 1 ≤ matrix[i][j] ≤ 1000

    [output] 2D integer array
    Matrix with the order of elements on its longest diagonals reversed. */


// function reverseOnDiagonals(matrix) {
//     let res = matrix.map(v => [...v])
//     for (let i = 0; i < matrix.length / 2; i++) {
//         let len = matrix.length-i-1
//         res[i][i] = matrix[len][len]
//         res[i][len] = matrix[len][i]
//         res[len][i] = matrix[i][len]
//         res[len][len] = matrix[i][i]
//     }
//     return res
// }

function reverseOnDiagonals(matrix) {
    for (let i = 0, j = matrix.length - 1; i < matrix.length / 2; i++, j--) {
        [matrix[i][i], matrix[j][j]] = [matrix[j][j], matrix[i][i]];
        [matrix[i][j], matrix[j][i]] = [matrix[j][i], matrix[i][j]];
    }
    return matrix
}

q = reverseOnDiagonals([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
//  [[9,2,7], [4,5,6],  [3,8,1]]
q
q = reverseOnDiagonals([[239]]) // [[239]]
q
q = reverseOnDiagonals([[1,10],  [100,1000]]) // [[1000,100],  [10,1]]
q
q = reverseOnDiagonals([[43,455,32,103],  [102,988,298,981],  [309,21,53,64],  [2,22,35,291]]) 
// [[291,455,32,2],  [102,53,21,981],  [309,298,988,64], [103,22,35,43]]
q