// Beta - Duplicate

/* Given an array of integers, find if the array contains any duplicate elements. 
The function should return true if any value appears at least twice in the array, and false if every element is distinct. */

const existsDuplicate = (numbers) => numbers.length !== new Set(numbers).size


q = existsDuplicate([4, 6, 7, 7, 1]) // true
q
q = existsDuplicate([4]) // false
q
q = existsDuplicate([]) // false
q
q = existsDuplicate([4, 3, 6, 1, 3, 6, 1, 3, 4, 5, 6, 1, 2, 3, 5, 1, 1]) // true
q
q = existsDuplicate([0]) // false
q