// 8kyu - Removing Elements

/* Take an array and remove every second element out of that array. 
Always keep the first element and start removing with the next element.

myArr = ['Keep', 'Remove', 'Keep', 'Remove', 'Keep', ...];

None of the arrays will be empty, so you don't have to worry about that! */

const removeEveryOther = (arr) => arr.filter((v, i) => i % 2 ? '' : v)

q = removeEveryOther(['Hello', 'Goodbye', 'Hello Again']) // ['Hello', 'Hello Again']
q
q = removeEveryOther([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) // [1, 3, 5, 7, 9]
q
q = removeEveryOther([ [1, 2] ]) // [[1, 2]]
q
q = removeEveryOther([['Goodbye'], {'Great': 'Job'}]) // [['Goodbye']]
q