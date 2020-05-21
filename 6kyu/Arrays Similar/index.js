// 6kyu - Arrays Similar

/* Write a function that determines whether the passed in arrays are similar. 
Similar means they contain the same elements, and the same number of occurrences of elements. */

function arraysSimilar(arr1, arr2) {
    arr1.sort((a, b) => a - b)
    arr2.sort((a, b) => a - b)
    return arr1.length > arr2.length ?
        arr1.every((v, i) => v === arr2[i]) :
        arr2.every((v, i) => v === arr1[i])
}

// const arraysSimilar = (arr1, arr2) => JSON.stringify(arr1.slice().sort()) === JSON.stringify(arr2.slice().sort())
// const arraysSimilar = (arr1, arr2) => arr1.sort().length == arr2.sort().length && arr1.every((el, i) => el === arr2[i]);

var arr1 = [1, 2, 2, 3, 4],
    arr2 = [2, 1, 2, 4, 3],
    arr3 = [1, 2, 3, 4],
    arr4 = [1, 2, 3, "4"]

q = arraysSimilar(arr1, arr2); // Should equal true
q
q = arraysSimilar(arr2, arr3); // Should equal false
q
q = arraysSimilar(arr3, arr4); // Should equal false
q