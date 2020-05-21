// function maxTriSum(numbers) {
//     numbers.sort((a,b) => b - a)
//     numbers

//     // dedup - remove all duplicates - via 3 different methods
//     let a = [...new Set(numbers)]
//     a

//     let b = numbers.filter((item, index) => numbers.indexOf(item) == index)
//     b

//     let c = numbers.reduce((unique, item) => unique.includes(item) ? unique : [...unique, item], [])
//     c

//     // compare two array - whether all items in a are equal to corresponding items in b
//     let d = JSON.stringify(a) == JSON.stringify(b)
//     d

//     let e = a.every((val, index) => val == b[index])
//     e

//     //

// }

// const maxTriSum = numbers => numbers.sort((a, b) => a - b)
//                                     .filter((value, index) => index == numbers.indexOf(value))
//                                 //  .reduce((unique, item) => unique.includes(item) ? unique : [...unique, item], [])
//                                     .slice(-3)
//                                     .reduce((a, b) => a + b)

// const maxTriSum = numbers => {
//     return [...new Set(numbers)].sort((a,b) => a-b).slice(-3).reduce((a,b) => a + b)
//     // const [a, b, c, ...rest] = [...new Set([...numbers])].sort((a, b) => b - a);
//     // return a + b + c
//     // return a
// }

const maxTriSum = nums => [...new Set(nums)].sort((a,b) => a-b).slice(-3).reduce((a,b) => a+b)

q = maxTriSum([3, 2, 6, 8, 2, 3]) // 17
q
q = maxTriSum([2, 9, 13, 10, 5, 2, 9, 5]) // 32
q
q = maxTriSum([2, 1, 8, 0, 6, 4, 8, 6, 2, 4]) // 18
q
q = maxTriSum([-3, -27, -4, -2, -27, -2]) // -9
q
q = maxTriSum([-14, -12, -7, -42, -809, -14, -12]) // -33
q
q = maxTriSum([-13, -50, 57, 13, 67, -13, 57, 108, 67]) // 232
q
q = maxTriSum([-7, 12, -7, 29, -5, 0, -7, 0, 0, 29]) // 41
q
q = maxTriSum([-2, 0, 2]) // 0
q
q = maxTriSum([-2, -4, 0, -9, 2]) // 0
q
q = maxTriSum([-5, -1, -9, 0, 2]) // 1
q