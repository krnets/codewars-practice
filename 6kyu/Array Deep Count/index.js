// 6kyu - Array Deep Count

/* Array.prototype.length will give you the number of top-level elements in an array.

Your task is to create a function deepCount that returns the number of ALL elements within an array, 
including any within inner-level arrays.

deepCount([1, 2, 3]);  
//>>>>> 3
deepCount(["x", "y", ["z"]]);  
//>>>>> 4
deepCount([1, 2, [3, 4, [5]]]);  
//>>>>> 7 */

const deepCount = a => a.reduce((acc, sub) => acc + (Array.isArray(sub) ? deepCount(sub) : 0), a.length)

q = deepCount([]) // 0, "Expected 0"
q
q = deepCount([1, 2, 3]) // 3, "Expected 3"
q
q = deepCount(["x", "y", ["z"]]) // 4, "Expected 4"
q
q = deepCount([1, 2, [3, 4, [5]]]) // 7, "Expected 7"
q
q = deepCount([[[[[[[[[]]]]]]]]]) // 8, "Expected 8"
q