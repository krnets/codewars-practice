// function sumOfDifferences(arr) {
//     let sum = 0
//     arr = arr.sort((a, b) => a - b)
//         // .forEach((sum, index) => {
//         //     sum += arr[index+1] - arr[index]
//         // })

//     for (let i = 0; i < arr.length - 1; i++) {
//         sum += arr[i + 1] - arr[i]
//     }

//     return sum
// }

const sumOfDifferences = arr => 
            arr.length > 1 ?
            Math.max(...arr) - Math.min(...arr) : 
            0

q = sumOfDifferences([1,2,10])
q
q = sumOfDifferences([-1,-2,-3])
q

// q = sumOfDifferences([-1, 6, 6, 20, -7, 14, 1, -7, 24, 9, 11, 6, 15, -21, 13, 11, -24, 15, 2, 25, 17, 9, 20, 10, -14, -18, 12])
// q

// let sum
// Test.describe("sumOfDifferences([1, 2, 10]", function() {
//     Test.assertEquals(sumOfDifferences([1, 2, 10]), 9);
//   });

//   Test.describe("sumOfDifferences([-3, -2, -1])", function() {
//     Test.assertEquals(sumOfDifferences([-3, -2, -1]), 2);
//   });