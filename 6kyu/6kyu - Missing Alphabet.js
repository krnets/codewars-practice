// 6kyu - Missing Alphabet

/* In this Kata you have to create a function,named insertMissingLetters,that takes in a string and 
outputs the same string processed in a particular way.

The function should insert only after the first occurence of each character of the input string, all the alphabet letters that:

-are NOT in the original string
-come after the letter of the string you are processing

Each added letter should be in uppercase, the letters of the original string will always be in lowercase.

input: "holly"
missing letters: "a,b,c,d,e,f,g,i,j,k,m,n,p,q,r,s,t,u,v,w,x,z"
output: "hIJKMNPQRSTUVWXZoPQRSTUVWXZlMNPQRSTUVWXZlyZ"

You don't need to validate input, the input string will always contain a certain amount of lowercase letters (min 1 / max 50). */

// function insertMissingLetters(str) {
//     let out = str.slice()
//     let uniq = [...new Set(str)]
//     let abc = [...'a'.repeat(26)].map((c, i) => String.fromCharCode(c.charCodeAt() + i)).join()
//     let arr = []
//     for (let c of uniq)
//         arr.push(c + abc.slice(abc.indexOf(c)).replace(new RegExp(`[${uniq}]`, 'gi'), '').toUpperCase())
//     for (let i = 0; i < uniq.length; i++)
//         out = out.replace(new RegExp(uniq[i]), arr[i])
//     return out
// }

const insertMissingLetters = str => [...str]
    .map((v, i, a) => i == a.indexOf(v) ?
        v + [...'a'.repeat(26)]
        .map((c, i) => String.fromCharCode(c.charCodeAt() + i))
        .filter(c => !str.includes(c) && c.charCodeAt() > v.charCodeAt())
        .join('')
        .toUpperCase() :
        v)
    .join('')

q = insertMissingLetters("hello") // "hIJKMNPQRSTUVWXYZeFGIJKMNPQRSTUVWXYZlMNPQRSTUVWXYZloPQRSTUVWXYZ"
q