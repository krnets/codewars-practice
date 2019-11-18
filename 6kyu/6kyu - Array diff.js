// 6kyu - Array.diff

/* Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.

It should remove all values from list a, which are present in list b.
If a value is present in b, all of its occurrences must be removed from the other */

// const array_diff = (a, b) => a.filter(v => !b.includes(v))
const array_diff = (a, b) => a.filter(v => b.indexOf(v) < 0)


q = array_diff([1, 2], [1]) // [2]
q
q = array_diff([1, 2, 2, 2, 3], [2]) // [1,3]
q
q = array_diff([], [4, 5]) // [], "a was [], b was [4,5]"
q
q = array_diff([3, 4], [3]) // [4], "a was [3,4], b was [3]"
q
q = array_diff([1, 8, 2], []) // [1,8,2], "a was [1,8,2], b was []"
q