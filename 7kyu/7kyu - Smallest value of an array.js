// 7kyu - Smallest value of an array

/* Write a function that can return the smallest value of an array or the index of that value. 
The function's 2nd parameter will tell whether it should return the value or the index.

Assume the first parameter will always be an array filled with at least 1 number and no duplicates. 
Assume the second parameter will be a string holding one of two values: 'value' and 'index'. */

const min = (arr, toReturn) => toReturn == 'value' ? v = Math.min(...arr) : arr.indexOf(v)

q = min([1,2,3,4,5], 'value') // => 1
q
q = min([1,2,3,4,5], 'index') // => 0
q