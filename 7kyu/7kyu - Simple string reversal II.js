// function solve(st, a, b) {
//     let begin = st.slice(0, a)
//     let middle = st.slice(a, b+1).split('').reverse().join('')
//     let end = st.slice(b+1)

//     return begin + middle + end
// }

// const solve = (st,a,b) => st.slice(0,a) + [...st.slice(a,b+1)].reverse().join`` + st.slice(b+1)
const solve = (st,a,b) => st.slice(0,a) + st.slice(a, b+1).split``.reverse().join`` + st.slice(b+1)

q = solve("codewars", 1, 5) // "cawedors"
q
q = solve("codingIsFun", 2, 100) // "conuFsIgnid"
q
q = solve("FunctionalProgramming", 2, 15) // "FuargorPlanoitcnmming"
q
q = solve("abcdefghijklmnopqrstuvwxyz", 0, 20) // "utsrqponmlkjihgfedcbavwxyz"
q
q = solve("abcdefghijklmnopqrstuvwxyz", 5, 20) // "abcdeutsrqponmlkjihgfvwxyz"
q