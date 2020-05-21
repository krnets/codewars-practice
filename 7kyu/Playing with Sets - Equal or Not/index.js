// 7kyu - Playing with Sets : Equal or Not ?

/* Two sets ( A, B ) are considered "equal" if all elements of A are elements of B and 
all elements of B are elements of A no matter "order" of elements.

  {1, 2} == {2, 1}
  {1, 2} != {1, 2, 3}

Create 2 functions, areEqual and notEqual, getting 2 sets as arguments and returning a true or false 
depending if these 2 sets are "equal" (respectively not equal) 
ie : if all elements of 1st set are elements of 2d and all elements of 2d set are elements of 1st. */

// function areEqual(s1, s2) {
//     let a1 = [...s1].sort((a, b) => a - b)
//     let a2 = [...s2].sort((a, b) => a - b)
//     for (let i of a1)
//         if (a1[i] != a2[i])
//             return false
//     return true
// }

// function areEqual(s1, s2) {
//     let a1 = [...s1].sort((a, b) => a - b)
//     let a2 = [...s2].sort((a, b) => a - b)
//     return a1.every(v => a2.includes(v)) && a1.length == a2.length
// }

const areEqual = (s1, s2) => s1.size == s2.size && [...s1].every(v => s2.has(v))
const notEqual = (s1, s2) => !areEqual(s1, s2)

// function notEqual(s1, s2) {
//     return !areEqual(s1, s2)
// }

// function notEqual(s1, s2) {
//     let a1 = [...s1].sort((a, b) => a - b)
//     let a2 = [...s2].sort((a, b) => a - b)
//     for (let i of a1)
//         if (a1[i] != a2[i])
//             return true
//     return false
// }


A = new Set([1, 2])
A2 = new Set([2, 1])
B = new Set([2, 3])

q = areEqual(A, B) // -> false
q
q = areEqual(A, A2) // -> true
q
q = areEqual(A2, A) // -> true
q
q = notEqual(A, B) // -> true
q

A1 = new Set([1, 2, 3])
A2 = new Set([3, 2, 1])
B = new Set([1, 2, 5])

q = areEqual(A1, A1) // "A == A"
q
q = areEqual(A1, A2) // "{1,2,3} == {3,2,1}"
q
q = areEqual(A2, A1) // "{3,2,1} == {1,2,3}"
q
q = !areEqual(A1, B) // "{1,2,3} != {1,2,5}"
q
q = notEqual(A1, B) // "{1,2,3} != {1,2,5}"
q
q = notEqual(A1, new Set()) // "{1,2,3} != {}"
q
q = !notEqual(A1, A2) // "{1,2,3} == {3,2,1}"
q