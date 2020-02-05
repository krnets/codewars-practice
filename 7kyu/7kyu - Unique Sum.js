// 7kyu - Unique Sum

/* Given a list of integers values, your job is to return the sum of the values; 
however, if the same integer value appears multiple times in the list, you can only count it once in your sum. */

const uniqueSum = (lst) => [...new Set(lst)].reduce((a, b) => a + b, null)

q = uniqueSum([1, 2, 3]) // 6
q
q = uniqueSum([1, 3, 8, 1, 8]) // 12
q
q = uniqueSum([-1, -1, 5, 2, -7]) // -1
q
q = uniqueSum([]) // null
q