// 6kyu - Pascal's Triangle

/* Write a function that, given a depth (n), returns a flat (single-dimensional)
array/list representing Pascal's Triangle from the first to the n-th level.

1
11
121
1331
14641

pascalsTriangle(4) == [1, 1, 1, 1, 2, 1, 1, 3, 3, 1]

Algorithms | Arrays | Mathematics | Numbers */

// function pascalsTriangle(n) {
//     let triangle = []
//     for (let row = 0; row < n; row++) {
//         triangle[row] = []
//         for (let idx = 0; idx <= row; idx++) {
//             if (idx == 0 || idx == row)
//                 triangle[row][idx] = 1
//             else
//                 triangle[row][idx] = triangle[row - 1][idx - 1] + triangle[row - 1][idx]
//         }
//     }
//     return triangle.reduce((a, b) => a.concat(b))
// }

// function pascalsTriangle(n) {
//     let triangle = [];
//     for (let row = 0; row < n; row++) {
//         let arr = [];
//         for (let idx = 0; idx < row + 1; idx++) {
//             if (idx == 0 || idx == row) arr.push(1)
//             else arr.push(triangle[row - 1][idx - 1] + triangle[row - 1][idx])
//         }
//         triangle.push(arr);
//     }
//     return triangle;
//     // return triangle.join(',');
// }

// function pascalsTriangle(n) {
//     let triangle = [];
//     for (let row = 0; row < n; row++) {
//         let num = 1;
//         for (let idx = 0; idx <= row; idx++) {
//             triangle.push(num);
//             num = num * (row - idx) / (idx + 1);
//         }
//     }
//     return triangle;
// }

// const pascalsTriangle = t = (n, l = []) => n ? [...(l = [1, ...l.map((x, i) => x + ~~l[i + 1])]), ...t(n - 1, l)] : []

function pascalsTriangle(n) {
    let res = [], row = [];
    for (let r = 0; r < n; ++r)
        res.push(row = row.map((e, i) => e + (row[i - 1] || 0)).concat([1]))
    return res.join(',').split(',')
}

q = pascalsTriangle(1) // [1]
q
q = pascalsTriangle(2) // [1,1,1]
q
q = pascalsTriangle(4) // [1,1,1,1,2,1,1,3,3,1]
q
q = pascalsTriangle(6) // [1,1,1,1,2,1,1,3,3,1,1,4,6,4,1,1,5,10,10,5,1]
q