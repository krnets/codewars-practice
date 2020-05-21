// 7kyu - Find sum of top-left to bottom-right diagonals

/* Given a square matrix (i.e. an array of subarrays), find the sum of values from the first value of the first array, 
the second value of the second array, the third value of the third array, and so on...

array = [[1, 2],
         [3, 4]]

diagonal sum: 1 + 4 = 5

array = [[5, 9, 1, 0],
         [8, 7, 2, 3],
         [1, 4, 1, 9],
         [2, 3, 8, 2]]

diagonal sum: 5 + 7 + 1 + 2 = 15 */

// function diagonalSum(matrix) {
//     for (var sum = 0, i = 0; i < matrix.length; i++)
//         for (var j = i; j <= i; j++)
//             sum += matrix[i][j]
//     return sum
// }

const diagonalSum = (matrix) => matrix.reduce((sum, v, i) => sum + v[i], 0)

q = diagonalSum([[12]]) // 12
q
q = diagonalSum([[1, 2], [3, 4]]) //  5
q
q = diagonalSum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) // 15
q
q = diagonalSum([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]) // 34
q