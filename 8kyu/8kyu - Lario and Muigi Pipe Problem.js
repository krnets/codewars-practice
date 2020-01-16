// 8kyu - Lario and Muigi Pipe Problem

/* Looks like some hoodlum plumber and his brother has been running around and damaging your stages again.
The pipes connecting your level's stages together need to be fixed before you recieve any more complaints. 
Each pipe should be connecting, since the levels ascend, you can assume every number in the sequence after 
the first index will be greater than the previous and that there will be no duplicates.
Given the a list of numbers, return the list so that the values increment by 1 for each index up to the maximum value.

Input: 1,3,5,6,7,8
Output: 1,2,3,4,5,6,7,8 */

// const pipeFix = (numbers) => Array(numbers.slice(-1) - numbers[0] + 1).fill().map((_, i) => numbers[0] + i)
// const pipeFix = (numbers) => Array.from({length: numbers.pop() - numbers[0] + 1}, (_, i) => i + numbers[0])
// const pipeFix = (numbers) => Array(numbers.pop() - numbers[0] + 1).fill().map((_,i) => i + numbers[0])

function pipeFix(numbers) {
    [arr, first, last] = [[], numbers[0], numbers[numbers.length - 1]]
    for (let i = first; i <= last; i++) arr.push(i)
    return arr
}

q = pipeFix([1, 2, 3, 5, 6, 8, 9]) // [1,2,3,4,5,6,7,8,9]
q
q = pipeFix([1, 2, 3, 12]) // [1,2,3,4,5,6,7,8,9,10,11,12]
q
q = pipeFix([6, 9]) // [6,7,8,9]
q
q = pipeFix([-1, 4]) // [-1,0,1,2,3,4]
q
q = pipeFix([1, 2, 3]) // [1,2,3]
q