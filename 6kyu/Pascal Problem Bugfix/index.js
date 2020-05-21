// 6kyu - Pascal Problem Bugfix

/* Here is a classic, Pascal's triangle.

The pascal function should return a nested array, such as in the example below,

pascal(5) // should return [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

However, when running the given code, the result is an empty array.

Your job? Fix it!
Bugs | Basic Language Features | Fundamentals */


// function pascal(depth) {
//     var results = [];
//     for (var r = 0; r < depth; r++) {
//         var temp = [];
//         for (var c = 0; c <= r; c++) {
//             if (c == 0 || c == r)
//                 temp.push(1);
//             else
//                 temp.push(results[r - 1][c - 1] + results[r - 1][c])
//         }
//         results.push(temp);
//     }
//     return results;
// }

function pascal(depth) {
    var results = [];
    var temp = [];
    for (var r = 0; r < depth; r++) {
        for (var c = 0; c <= r; c++) {
            temp.push(calculate(c, r));
        }
        results.push(temp);
        temp = [];
    }
    return results;
}

function calculate(c, r) {
    if (c == r || c == 0)
        return 1;
    else
        return calculate(c - 1, r - 1) + calculate(c, r - 1);
}

q = pascal(1) // [[1]]
q
q = pascal(4) // [[1],[1,1],[1,2,1],[1,3,3,1]]
q