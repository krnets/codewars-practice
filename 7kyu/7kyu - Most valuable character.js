// 7kyu - Most valuable character

/* In this Kata, you will be given a string and your task is to return the most valuable character. 
The value of a character is the difference between the index of its last occurrence and 
the index of its first occurrence. Return the character that has the highest value. 
If there is a tie, return the lexicographically lowest character.

All inputs will be lower case.  */

function solve(st) {
    let indexDiff = [...new Set([...st])].map(c => [c, st.lastIndexOf(c) - st.indexOf(c)])
    let highest = indexDiff.sort((a, b) => (c = b[1] - a[1]) == 0 ? a[0].localeCompare(b[0]) : c)
    return highest[0][0]
}

// const solve = st =>  [...st].reduce((res, ch) => { const max = st.lastIndexOf(ch) - st.indexOf(ch);
//         return (max > res.max || max === res.max && ch < res.ch) ? { max, ch } : res; }, { max: 0, ch: st[0] }).ch;


q = solve('a') // 'a'
q
q = solve('aa') // 'a'
q
q = solve('bcd') // 'b'
q
q = solve('axyzxyz') // 'x'
q
q = solve('aabccc') // 'c'
q