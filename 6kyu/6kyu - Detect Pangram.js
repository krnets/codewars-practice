// 6kyu - Detect Pangram

/* A pangram is a sentence that contains every single letter of the alphabet at least once. 
For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, 
because it uses the letters A-Z at least once (case is irrelevant).
Given a string, detect whether or not it is a pangram. Return True if it is, 
False if not. Ignore numbers and punctuation. */

// function isPangram(string) {
//     let res = [];
//     [...string.replace(/\W|\d/g, '').toLowerCase()].forEach(v => res.push(v))
//     return Array.from(new Set(res)).length == 26
// }

// const isPangram = string => [...string.replace(/\W/g, '')].map(v => /[a-z]/gi.test(v))
// const isPangram = string => [...string.replace(/\W/g, '')].every(v => /[a-z]/gi.test(v))
// const isPangram = string => {
//     string = string.toLowerCase();
//     // return [...'abcdefghijklmnopqrstuvwxyz'].every(v => string.indexOf(v) != -1)
//     return [...'abcdefghijklmnopqrstuvwxyz'].every(v => string.includes(v))
// }
// const isPangram = string => (s = string.toLowerCase(), [...'abcdefghijklmnopqrstuvwxyz'].every(v => s.indexOf(v) != -1))
const isPangram = string => (s = string.toLowerCase(), [...'abcdefghijklmnopqrstuvwxyz'].every(v => s.includes(v)))
// const isPangram = string => (string.match(/([a-z])(?!.*\1)/ig) || []).length == 26


q = isPangram('The quick brown fox jumps over the lazy dog.') // true
q

q = isPangram('This is not a pangram.') // false
q

q = isPangram('ABCD45EFGH,IJK,LMNOPQR56STUVW3XYZ') // true
// is  a pangram (a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z missing)
q