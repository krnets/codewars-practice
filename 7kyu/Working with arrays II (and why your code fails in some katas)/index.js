// 7kyu - Working with arrays II (and why your code fails in some katas)

/* In this kata the function returns an array/list like the one passed to it 
but with its nth element removed (with 0 <= n <= array/list.length - 1). 
The function is already written for you and the basic tests pass, but random tests fail. 
Your task is to figure out why and fix it. */

function removeNthElement(arr, n) {
    let arrCopy = arr.slice()
    arrCopy.splice(n, 1)
    return arrCopy
}

q = removeNthElement([1, 2, 3, 4, 5], 4) // [1, 2, 3, 4]
q
q = removeNthElement([9, 7, 6, 9], 0) // [7, 6, 9]
q
q = removeNthElement([4, 6, 83, 57, 35, 71, 93, 18, 14], 6) // [4, 6, 83, 57, 35, 71, 14]
q
q = removeNthElement([54, 3, 3, 15, 44, 82, 13], 1) // [54, 15, 44, 82, 13]
q