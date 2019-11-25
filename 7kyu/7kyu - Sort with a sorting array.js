// 7kyu - Sort with a sorting array

/* Sort an array according to the indices in another array. 
It is guaranteed that the two arrays have the same size, 
and that the sorting array has all the required indices.

initialArray = ['x', 'y', 'z'] sortingArray = [ 1, 2, 0]
sort(initialArray, sortingArray) => ['z', 'x', 'y']
sort(['z', 'x', 'y'], [0, 2, 1]) => ['z', 'y', 'x'] */


// function sort(initialArray, sortingArray) {
//     for (var arr = [], i = 0; i < initialArray.length; i++)
//         arr[sortingArray[i]] = initialArray[i]
//     return arr
// }

// const sort = (initialArray, sortingArray) => [...Array(initialArray.length)].map((_, i) => initialArray[sortingArray.indexOf(i)])
// const sort = (initialArray, sortingArray) => initialArray.reduce((newArray, v, i) => (newArray[sortingArray[i]] = v, newArray), [])

// function sort(initialArray, sortingArray) {
//     let newArray = [];
//     sortingArray.forEach((v, i) => newArray[v] = initialArray[i])
//     return newArray
// }

// function sort(initialArray, sortingArray) {
//     let newArray = [];
//     initialArray.forEach((v, i) => newArray[sortingArray[i]] = v)
//     return newArray
// }

// function sort(initialArray, sortingArray) {
//     let result = []
//     for (let [i, j] of Object.entries(sortingArray))
//         result.push(initialArray[j])
//     return result
// }

// function sort(initialArray, sortingArray) {
//     let result = []
//     for (let [i, j] of Object.entries(sortingArray))
//         result[i] = initialArray[j]
//     return result
// }

const sort = (initialArray, sortingArray) => initialArray.map((v, i) => ({
    value: v,
    index: sortingArray[i]
})).sort((a, b) => a.index - b.index).map(v => v.value)

q = sort([1, 2, 3, 4, 5], [0, 2, 1, 4, 3]) // [1, 3, 2, 5, 4]
q

q = sort(['z', 'x', 'y'], [0, 2, 1]) // ['z', 'y', 'x']
q