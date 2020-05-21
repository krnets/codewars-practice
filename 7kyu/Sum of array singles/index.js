// 7kyu - Sum of array singles

/* In this Kata, you will be given an array of numbers in which two numbers occur once 
and the rest occur only twice. Your task will be to return the sum of the numbers that occur only once.

For example, repeats([4,5,7,5,4,8]) = 15 because only the numbers 7 and 8 occur once, and their sum is 15. */

// function repeats(arr) {
//     for (var res = 0, i = 0; i < arr.length; i++)
//         if (arr.indexOf(arr[i]) == arr.lastIndexOf(arr[i]))
//             res += arr[i]
//     return res
// }

const repeats = (arr) => arr.filter(v => arr.indexOf(v) == arr.lastIndexOf(v)).reduce((a, b) => a + b, 0)

q = repeats([4, 5, 7, 5, 4, 8]) // 15
q
q = repeats([9, 10, 19, 13, 19, 13]) // 19
q
q = repeats([16, 0, 11, 4, 8, 16, 0, 11]) // 12
q
q = repeats([5, 17, 18, 11, 13, 18, 11, 13]) // 22
q
q = repeats([5, 10, 19, 13, 10, 13]) // 24
q