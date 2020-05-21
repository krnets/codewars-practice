// function arrayMash(array1, array2) {
//     let mergedArray = []
//     for (let i = 0; i < array1.length; i++)
//         mergedArray.push(array1[i], array2[i])
//     return mergedArray
// }

const arrayMash = (array1, array2) => array1.reduce((mashed, el, i) => mashed.concat(el, array2[i]), [])

q = arrayMash([1, 2, 3], ['a', 'b', 'c']) // [1, 'a', 2, 'b', 3, 'c']
q
q = arrayMash([1, 2, 3, 4, 5], ['a', 'b', 'c', 'd', 'e']) // [1, 'a', 2, 'b', 3, 'c', 4, 'd', 5, 'e']
q
q = arrayMash([1, 1, 1, 1], [2, 2, 2, 2]) // [1, 2, 1, 2, 1, 2, 1, 2]
q
q = arrayMash([1, 8, 'hello', 'dog'], ['fish', '2', 9, 10]) // [1, "fish", 8, "2", "hello", 9, "dog", 10]
q
q = arrayMash([null, null, 4], [NaN, null, 'hello']) // [null, NaN, null, null, 4, "hello"]
q
q = arrayMash([1], [2]) // [1, 2]
q
q = arrayMash(['h', 'l', 'o', 'o', 'l'], ['e', 'l', 'w', 'r', 'd']) // ["h", "e", "l", "l", "o", "w", "o", "r", "l", "d"]
q