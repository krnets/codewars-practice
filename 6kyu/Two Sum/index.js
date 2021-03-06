// 6kyu - Two Sum

/* Write a function that takes an array of numbers (integers for the tests) and a target number. 
It should find two different items in the array that, when added together, give the target value. 
The indices of these items should then be returned in a tuple like so: (index1, index2).

For the purposes of this kata, some tests may have multiple answers; any valid solutions will be accepted.

The input will always be valid (numbers will be an array of length 2 or greater, and all of the items will be numbers; 
target will always be the sum of two different items from that array). */

// function twoSum(number, target) {
//     let res = []
//     for (let i = 0; i < number.length; i++) {
//         for (let j = 1; j < number.length; j++) {
//             if (number[i] + number[j] == target) {
//                 res.push(i)
//                 res.push(j)
//             }
//         }
//     }
//     return res.slice(0, 2)
// }

function twoSum(number, target) {
    for (let i = 0; i < number.length; i++)
        for (let j = 1; j < number.length; j++)
            if (number[i] + number[j] == target)
                return [i, j]
}

// function twoSum(number, target) {
//     let valsMap = new Map()
//     for (let i = 0; i < number.length; i++) {
//         let complement = target - number[i]
//         if (valsMap.get(complement) != undefined)
//             return [valsMap.get(complement), i]
//         else 
//             valsMap.set(number[i], i)
//     }
// }

q = twoSum([1, 2, 3], 4) //  [0,2]
q
q = twoSum([1234, 5678, 9012], 14690) // [1,2]
q
q = twoSum([2, 2, 3], 4) // [0,1]
q