// 6kyu - Find the unique number (harder version - time constrained)

const findUnique = arr => arr.reduce((a, b) => a ^ b)


q = findUnique([1, 8, 4, 4, 6, 1, 8]) // 6
q
q = findUnique([1234567]) // 1234567
q
q = findUnique([1, 4, 4, 5, 5, 3, 3, 2, 2]) // 1
q
q = findUnique([2, 2, 5, 5, 4, 3, 3, 1, 1]) // 4
q
q = findUnique([3, 5, 5, 4, 4, 3, 2, 2, 9]) // 9
q