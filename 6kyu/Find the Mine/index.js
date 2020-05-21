// 6kyu - Find the Mine!

/* You've just discovered a square (NxN) field and you notice a warning sign. 
The sign states that there's a single bomb in the 2D grid-like field in front of you.

Write a function mineLocation/MineLocation that accepts a 2D array, and returns the location of the mine. 
The mine is represented as the integer 1 in the 2D array. Areas in the 2D array that are not the mine will be represented as 0s.

The location returned should be an array (Tuple<int, int> in C#) where the first element is the row index, 
and the second element is the column index of the bomb location (both should be 0 based). 
All 2D arrays passed into your function will be square (NxN), and there will only be one mine in the array.

mineLocation( [ [1, 0, 0], [0, 0, 0], [0, 0, 0] ] ) => returns [0, 0]
mineLocation( [ [0, 0, 0], [0, 1, 0], [0, 0, 0] ] ) => returns [1, 1]
mineLocation( [ [0, 0, 0], [0, 0, 0], [0, 1, 0] ] ) => returns [2, 1]   */

// function mineLocation(field) {
//     for (let i = 0; i < field.length; i++)
//         for (let j = 0; j < field.length; j++)
//             if (field[i][j] == 1)
//                 return [i, j]
// }

function mineLocation(field) {
    let len = field.length
    let index = field.join().split(',').indexOf('1')
    return [~~(index / len), index % len]
}

// const mineLocation = (field, loc) => (field.every((row, x) => row.every((col, y) => col == 0 || (loc = [x, y]))), loc)

// const mineLocation = field => field.reduce((r, v, i) => v.includes(1) ? [...r, i, v.indexOf(1)] : r, []);
// const mineLocation = field => field.reduce((coords, row, i) => row.indexOf(1) >= 0 ? [i, row.indexOf(1)] : coords, [])
// const mineLocation = field => field.reduce((coords, row, i) => row.includes(1)  ? [i, row.indexOf(1)] : coords, [])

q = mineLocation([ [1, 0], [0, 0] ]) // [0, 0]
q
q = mineLocation([ [1, 0, 0], [0, 0, 0], [0, 0, 0] ]) // [0, 0]
q
q = mineLocation([ [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0] ]) // [2, 2]
q