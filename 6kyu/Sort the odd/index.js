// 6kyu - Sort the odd

/* Your task is to sort ascending odd numbers but even numbers must be on their places.
Zero isn't an odd number and you don't need to move it. If you have an empty array, you need to return it. */


// function sortArray(array) {
//     let oddIndex = array.map((v, i) => v % 2 ? i : '_').filter(v => v != '_')
//     let oddSorted = array.filter(v => v % 2).sort((a, b) => a - b)

//     for (let i = 0; i < oddIndex.length; i++)
//         array[oddIndex[i]] = oddSorted[i]

//     return array
// }

// function sortArray(array) {
//     const odd = array.filter(v => v % 2).sort((a, b) => a - b);
//     return array.map(v => v % 2 ? odd.shift() : v);
// }

// function sortArray(array) {
//     let odd = array.filter(v => v % 2).sort((a, b) => b - a)
//     return array.map(v => v % 2 ? odd.pop() : v)
// }

const sortArray = array => (odd = array.filter(v => v % 2).sort((a, b) => b - a), array.map(v => v % 2 ? odd.pop() : v))


q = sortArray([5, 3, 2, 8, 1, 4]) // [1, 3, 2, 8, 5, 4]
q
q = sortArray([5, 3, 1, 8, 0]) // [1, 3, 5, 8, 0]
q
q = sortArray([]) // []
q