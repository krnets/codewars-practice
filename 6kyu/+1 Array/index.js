// 6kyu - +1 Array

/* Given an array of integers of any length, return an array that has 1 added to the value represented by the array.

    the array can't be empty
    only non-negative, single digit integers are allowed

Return nil (or your language's equivalent) for invalid inputs.
Examples

For example the array [2, 3, 9] equals 239, adding one would return the array [2, 4, 0].

[4, 3, 2, 5] would return [4, 3, 2, 6]  */

// const upArray = (arr) => arr.length && arr.every(v => v > -1 && String(v).length < 2) ? [...String(+arr.join('') + 1)].map(Number) : null

// const upArray = arr => arr.length && arr.every(v => v >= 0 && v < 10) && (arr.join('').slice(0, -10) + String(+arr.join('').slice(-10) + 1)).split('').map(Number) || null

function upArray(arr) {
    if (!arr.length || arr.some(n => n < 0 || n > 9)) return null;
    for (let i = arr.length - 1; i >= 0; i--) {
        if (arr[i] < 9) {
            arr[i]++;
            return arr;
        } else arr[i] = 0;
    }
    return [1, ...Array(arr.length).fill(0)]
}

q = upArray([2, 3, 9]) // [2,4,0]
q
q = upArray([4, 3, 2, 5]) // [4,3,2,6]
q
q = upArray([1, -9]) // null
q