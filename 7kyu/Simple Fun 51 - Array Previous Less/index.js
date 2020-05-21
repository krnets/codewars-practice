// 7kyu - Simple Fun #51: Array Previous Less

/* Given array of integers, for each position i, search among the previous positions for the last 
(from the left) position that contains a smaller value. Store this value at position i in the answer. 
If no such value can be found, store -1 instead.

For items = [3, 5, 2, 4, 5], the output should be [-1, 3, -1, 2, 4].

    [input] integer array arr
    Non-empty array of positive integers.

    Constraints: 3 ≤ arr.length ≤ 1000, 1 ≤ arr[i] ≤ 1000.

    [output] an integer array
    Array containing answer values computed as described above. */

// const arrayPreviousLess = (arr) => arr.map((v, i) => (s = arr.slice(0, i).filter(x => x < v), s.length) ? s[s.length - 1] : -1)
const arrayPreviousLess = (arr) => arr.map((v, i) => arr.slice(0, i).reverse().find(x => x < v) || -1)

q = arrayPreviousLess([3, 5, 2, 4, 5]) // [-1, 3, -1, 2, 4]
q
q = arrayPreviousLess([2, 2, 1, 3, 4, 5, 5, 3]) // [-1, -1, -1, 1, 3, 4, 4, 1]
q
q = arrayPreviousLess([3, 2, 1]) // [-1, -1, -1]
q