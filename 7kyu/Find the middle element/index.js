// 7kyu - Find the middle element

// function gimme(inputArray) {
//     let clone = Array.from(inputArray)
//     let midIndex = Math.floor(clone.length / 2)
//     clone.sort((a, b) => a - b)

//     return inputArray.indexOf(clone[midIndex])
// }

// const gimme = inputArray => inputArray.indexOf(inputArray.slice().sort((a, b) => a - b)[~~(inputArray.length / 2)])
// const gimme = inputArray => inputArray.indexOf(inputArray.concat().sort((a, b) => a - b)[~~(inputArray.length / 2)])
const gimme = inputArray => inputArray.indexOf([...inputArray].sort((a, b) => a - b)[~~(inputArray.length / 2)])


q = gimme([2, 3, 1]) // 0
q
q = gimme([5, 10, 14]) // 1
q