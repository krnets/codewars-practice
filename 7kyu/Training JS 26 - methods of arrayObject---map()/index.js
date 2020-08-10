// 7kyu - Training JS #26: methods of arrayObject---map()

/* Coding in function isolateIt. function accept 1  parameters arr, it's a string array. 
Your task is to put a character "|" into the middle of each element. 

If the string length is an even number, use the insert method.
"abcd" should became "ab|cd". "|" should be inserted between ab and cd.

If the string length is an odd number, use the replacement method. 
"abcde" should became "ab|de". Character c will be replaced by |.

The original array should not be changed, you need to return a new array
(if you use the map method, you do not need to worry about this).
Flexible use of slice() Will make the work more simple. */

// const isolateIt = arr => arr.map(s => s.slice(0, Math.floor(s.length / 2)) + '|' + s.slice(Math.ceil(s.length / 2)))
// const isolateIt = arr => arr.map(s => `${s.slice(0, Math.floor(s.length / 2))}|${s.slice(Math.ceil(s.length / 2))}`)
const isolateIt = arr => arr.map(s => s.slice(0, s.length / 2) + '|' + s.slice(-s.length / 2))


q = isolateIt(["abcd", "efgh"]) // ["ab|cd","ef|gh"]
q
q = isolateIt(["abcde", "fghij"]) // ["ab|de","fg|ij"]
q
q = isolateIt(["1234", "56789"]) // ["12|34","56|89"]
q