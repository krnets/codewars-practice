// 7kyu - Simple Fun #67: Array Change

/* You are given an array of integers. On each move you are allowed to increase exactly one of its element by one. 
Find the minimal number of moves required to obtain a strictly increasing sequence from the input.

For arr = [1, 1, 1], the output should be 3.

    [input] integer array arr

    Constraints:
    3 ≤ inputArray.length ≤ 100, -10000 ≤ inputArray[i] ≤ 10000.

    [output] an integer

    The minimal number of moves needed to obtain a strictly increasing sequence from inputArray.

    It's guaranteed that for the given test cases the answer always fits signed 32-bit integer type. */

function arrayChange(arr) {
    for (var count = 0, i = 1; i < arr.length; i++) {
        while (arr[i - 1] >= arr[i]) {
            arr[i]++
            count++
        }
    }
    return count
}

q = arrayChange([1, 2, 3]) // 
q
q = arrayChange([1, 1, 1]) // 3
q
q = arrayChange([-1000, 0, -2, 0]) // 5
q
q = arrayChange([2, 1, 10, 1]) // 12
q
q = arrayChange([2, 3, 3, 5, 5, 5, 4, 12, 12, 10, 15]) // 13
q