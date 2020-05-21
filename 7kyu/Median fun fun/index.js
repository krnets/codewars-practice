// 7kyu - Median fun fun

/* The mean (or average) is the most popular measure of central tendency; 
however it does not behave very well when the data is skewed (i.e. wages distribution). 
In such cases, it's better to use the median.

Your task for this kata is to find the median of an array consisting of n elements.

You can assume that all inputs are arrays of numbers in integer format. 
For the empty array your code should return NaN (false in JavaScript).

Input [1, 2, 3, 4] --> Median 2.5
Input [3, 4, 1, 2, 5] --> Median 3   */

// function median(arr) {
//     arr.sort((a, b) => a - b)
//     let left = Math.max(...arr.slice(0, arr.length / 2))
//     let right = Math.min(...arr.slice(arr.length / 2))
//     let mid = Math.floor(arr.length / 2)
//     return arr.length == 0 ? false : arr.length % 2 == 0 ? (left + right) / 2 : arr[mid]

function median(arr) {
    arr.sort((a, b) => a - b)
    let mid = Math.floor(arr.length / 2)
    return arr.length ? arr.length % 2 ? arr[mid] : (arr[mid - 1] + arr[mid]) / 2 : false
}

// const median = (n) => (n.sort((a, b) => a - b), mid = Math.floor(n.length / 2), n.length ? n.length % 2 ? n[mid] : (n[mid - 1] + n[mid]) / 2 : false)
// const median = (n) => (n.sort((a, b) => a - b), mid = ~~(n.length / 2), n.length ? n.length % 2 ? n[mid] : (n[mid - 1] + n[mid]) / 2 : false)

q = median([22, 65, 90, 11, 88, 98, 99, 87, 39, 50, 91, 16, 67, 64, 36, 81, 97, 40, 82, 91]) // 74
q
q = median([33, 48, 28, 33, 26, 62, 54, 71, 48, 64]) // 48
q
q = median([8, 43, 98, 11, 9, 92, 59, 34, 75, 10, 31, 2, 18, 77, 9, 9, 82, 82, 81, 13]) // 32.5
q
q = median([1, 2, 3, 4]) // 2.5
q
q = median([3, 4, 1, 2, 5]) // 3
q
q = median([10, 29, 23, 94, 76, 96, 5, 85, 4, 33, 47, 41, 87]) // 41
q
q = median([]) // false
q