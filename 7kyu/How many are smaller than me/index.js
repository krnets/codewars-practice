// 7kyu - How many are smaller than me?

/* Write function when given an array, returns the amount of numbers that are smaller than arr[i] to the right.

smaller([5, 4, 3, 2, 1]) === [4, 3, 2, 1, 0]
smaller([1, 2, 0]) === [1, 1, 0]  */

// function smaller(nums) {
//     return nums.map((v, i) => nums.slice(i + 1).filter(x => v > x).length)
// }

const smaller = (nums) => nums.map((x, i) => nums.slice(i + 1).filter(y => x > y).length)

q = smaller([5, 4, 3, 2, 1]) // [4, 3, 2, 1, 0]
q
q = smaller([1, 2, 3]) // [0, 0, 0]
q
q = smaller([1, 2, 0]) // [1, 1, 0]
q
q = smaller([1, 2, 1]) // [0, 1, 0]
q
q = smaller([1, 1, -1, 0, 0]) // [3, 3, 0, 0, 0]
q
q = smaller([5, 4, 7, 9, 2, 4, 4, 5, 6]) // [4, 1, 5, 5, 0, 0, 0, 0, 0]
q