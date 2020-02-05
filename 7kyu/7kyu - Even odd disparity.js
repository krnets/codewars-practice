// 7kyu - Even odd disparity

/* Given an array, return the difference between the count of even numbers and the count of odd numbers. 
0 will be considered an even number.

solve([0,1,2,3]) = 0 because there are two even numbers and two odd numbers. Even - Odd = 2 - 2 = 0.  

Let's now add two letters to the last example:

solve([0,1,2,3,'a','b']) = 0. Again, Even - Odd = 2 - 2 = 0. Ignore letters. 

The input will be an array of lowercase letters and numbers only.  */

// function solve(a) {
//     let even = a.filter(v => Number.isInteger(v) && v % 2 == 0).length
//     let odd = a.filter(v => Number.isInteger(v) && v % 2 != 0).length
//     return even - odd
// }

const solve = (a) => a.reduce((x, v) => Number.isInteger(v) ? (v % 2 == 0 ? x + 1 : x - 1) : x, 0)
// const solve = (a) => a.reduce((x, v) => Number.isInteger(v) ? x + (v % 2 == 0 ? 1 : -1) : x, 0)

q = solve([0, 1, 2, 3]) // 0
q
q = solve([0, 1, 2, 3, 'a', 'b']) // 0
q
q = solve([0, 15, 'z', 16, 'm', 13, 14, 'c', 9, 10, 13, 'u', 4, 3]) // 0
q
q = solve([13, 6, 8, 15, 4, 8, 13]) // 1
q
q = solve([1, 'a', 17, 8, 'e', 3, 'i', 12, 1]) // -2
q
q = solve([5, 15, 16, 10, 6, 4, 16, 't', 13, 'n', 14, 'k', 'n', 0, 'q', 'd', 7, 9]) // 2
q