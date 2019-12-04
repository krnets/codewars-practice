// 6kyu - Fold an array

/* In this kata you have to write a method that folds a given array of integers by the middle x-times.
An example says more than thousand words:

Fold 1-times:
[1,2,3,4,5] -> [6,6,3]

A little visualization (NOT for the algorithm but for the idea of folding):
 Step 1         Step 2        Step 3       Step 4       Step5
                     5/           5|         5\          
                    4/            4|          4\      
1 2 3 4 5      1 2 3/         1 2 3|       1 2 3\       6 6 3
----*----      ----*          ----*        ----*        ----*

Fold 2-times:
[1,2,3,4,5] -> [9,6]

As you see, if the count of numbers is odd, the middle number will stay. 
Otherwise the fold-point is between the middle-numbers, so all numbers would be added in a way.

The array will always contain numbers and will never be null. The parameter runs will always be a 
positive integer greater than 0 and says how many runs of folding your method has to do.

If an array with one element is folded, it stays as the same array.
The input array should not be modified! */

// function foldArray(array, runs) {
//     let result = []
//     let clone = array.slice()
//     while (clone.length)
//         result.push(clone.pop() + (clone.shift() || 0))
//     return runs - 1 ? foldArray(result, runs - 1) : result
// }

// function foldArray(array, runs) {
//     let c = array.slice()
//     while (runs > 0) {
//         let arr2 = c.splice(Math.ceil(c.length / 2)).reverse()
//         c = c.reduce((a, v, i) => [...a, arr2[i] ? v + arr2[i] : v], []);
//         runs--
//     }
//     return c
// }

// const foldArray = (a, runs) => Array(~~(a.length / 2))
//     .fill().map((_, i) => a[i] + a[a.length - i - 1])
//     .concat(a.length % 2 == 1 ? [a[(a.length - 1) / 2]] : [])

const foldArray = (a, runs) => runs == 0 ? a :
    foldArray(Array(~~(a.length / 2))
        .fill().map((_, i) => a[i] + a[a.length - i - 1])
        .concat(a.length % 2 == 1 ? [a[(a.length - 1) / 2]] : []), runs - 1);


var input = [1, 2, 3, 4, 5];
q = foldArray(input, 1) //  [ 6, 6, 3 ];
q
q = foldArray(input, 2) // expected = [ 9, 6 ];
q
q = foldArray(input, 3) // expected = [ 15 ];
q
input = [-9, 9, -8, 8, 66, 23];
q = foldArray(input, 1) // expected = [ 14, 75, 0 ];
q