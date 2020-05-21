// 7kyu - Matrix creation

/* Create an identity matrix of the specified size( >= 0).

Some examples:

(1)  =>  [[1]]

(2) => [ [1,0],
         [0,1] ]

       [ [1,0,0,0,0],
         [0,1,0,0,0],
(5) =>   [0,0,1,0,0],
         [0,0,0,1,0],
         [0,0,0,0,1] ]    */


// function getMatrix(number) {
//     let matrix = []
//     for (let row = 0; row < number; row++) {
//         matrix[row] = []
//         for (let col = 0; col < number; col++) {
//             if (row == col) matrix[row].push(1)
//             else matrix[row].push(0)
//         }
//     }
//     return matrix
// }

// function getMatrix(number) {
//     let matrix = []
//     for (let i = 0; i < number; i++) {
//         matrix[i] = Array(number).fill(0)
//         matrix[i][i] = 1
//     }
//     return matrix
// }

const getMatrix = n => [...Array(n)].map((_, row) => [...Array(n)].map((_, col) => Number(row == col)))

q = getMatrix(1) // [[1]]
q
q = getMatrix(2) // [[1, 0], [0, 1]]
q
q = getMatrix(5) // [[1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]
q