// 7kyu - No oddities here

/* Write a small function that returns the values of an array that are not odd.

All values in the array will be integers. Return the good values in the order they are given. */

const noOdds = values => values.filter(v => v % 2 == 0)

q = noOdds([2, 3, 4, 5, 6, 7]) // [2,4,6]
q