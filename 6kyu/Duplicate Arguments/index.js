// 6kyu - Duplicate Arguments

/* Complete the solution so that it returns true if it contains any duplicate argument values. 
Any number of arguments may be passed into the function.

The array values passed in will only be strings or numbers. The only valid return values are true and false.

solution(1, 2, 3)             -->  false
solution(1, 2, 3, 2)          -->  true
solution('1', '2', '3', '2')  -->  true */

// function solution() {
//     return [...arguments].filter((v, i, a) => a.indexOf(v) !== i).length > 0
// }

// function solution() {
//     return new Set(arguments).size != arguments.length;
// }

const solution = (...args) => args.length !== new Set(args).size


q = solution(1, 2, 3) // false
q
q = solution(1, 2, 3, 6, 5, 6) // true
q
q = solution('a', 'b', 'c', 'a') // true
q
q = solution(1, 2, 3, 'a', 'b') // false
q