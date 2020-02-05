// 7kyu - MinMinMax

/* Given an unsorted array of integers, find the smallest number in the array, the largest number in the array, 
and the smallest number between the two array bounds that is not in the array.

For instance, given the array [-1, 4, 5, -23, 24], the smallest number is -23, the largest number is 24, 
and the smallest number between the array bounds is -22. You may assume the input is well-formed.

You solution should return an array [smallest, minimumAbsent, largest]
The smallest integer should be the integer from the array with the lowest value.
The largest integer should be the integer from the array with the highest value.
The minimumAbsent is the smallest number between the largest and the smallest number that is not in the array. */

// function minMinMax(array) {
//     let smallest = Math.min(...array)
//     let largest = Math.max(...array)
//     for (let i = smallest; i < largest; i++) {
//         if (!array.includes(i)) {
//             var minimumAbsent = i
//             break
//         }
//     }
//     return [smallest, minimumAbsent, largest]
// }

function minMinMax(array) {
    let min = Math.min(...array)
    let max = Math.max(...array)
    for (let i = min; i < max; i++)
        if (!array.includes(i))
            return [min, i, max]
}

q = minMinMax([-1, 4, 5, -23, 24]) // [-23, -22, 24]
q
q = minMinMax([1, 3, -3, -2, 8, -1]) // [-3, 0, 8]
q
q = minMinMax([2, -4, 8, -5, 9, 7]) // [-5, -3, 9]
q