// freeCodeCamp problem

// function largestOfFour(arr) {
//     var results = [];
//     // var temp = arr.length
//     // temp

//     for (var n = 0; n < arr.length; n++) {
//         // n

//         var largestNumber = arr[n][0];
//         // largestNumber

//         for (var sb = 1; sb < arr[n].length; sb++) {
//             // temp = arr[n][sb]
//             // temp
//             if (arr[n][sb] > largestNumber) {
//                 largestNumber = arr[n][sb];
//                 // largestNumber
//             }
//         }

//         // largestNumber
//         // results

//         results[n] = largestNumber;
//         // results
//     }
//     // results
//     return results;
// }

// const largestOfFour = mainArray =>
//     mainArray.map(subArray => subArray
//         .reduce((prev, curr) =>
//             curr > prev ?
//             curr : prev))

// const largestInt = arr =>
//     arr.reduce((prev, curr) =>
//         prev < curr ?
//         curr : prev, 0)


// q = largestInt([13, 27, 18, 26])
// q
// q = largestOfFour([
//     [4, 5, 1, 3],
//     [13, 27, 18, 26],
//     [32, 35, 37, 39],
//     [1000, 1001, 857, 1]
// ]);
// q

const largestOfFour = arr => arr.map(Function.apply.bind(Math.max, null))

q = largestOfFour([
    [4, 5, 1, 3],
    [13, 27, 18, 26],
    [32, 35, 37, 39],
    [1000, 1001, 857, 1]
])
// should return an array.
q
// q = largestOfFour([
//     [13, 27, 18, 26],
//     [4, 5, 1, 3],
//     [32, 35, 37, 39],
//     [1000, 1001, 857, 1]
// ])
// // [27, 5, 39, 1001].
// q
// q = largestOfFour([
//     [4, 9, 1, 3],
//     [13, 35, 18, 26],
//     [32, 35, 97, 39],
//     [1000000, 1001, 857, 1]
// ])
// // should return [9, 35, 97, 1000000].
// q
// q = largestOfFour([
//     [17, 23, 25, 12],
//     [25, 7, 34, 48],
//     [4, -10, 18, 21],
//     [-72, -3, -17, -10]
// ])
// // should return [25, 48, 21, -3].
// q    