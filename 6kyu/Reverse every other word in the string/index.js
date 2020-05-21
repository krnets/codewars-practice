// 6kyu - Reverse every other word in the string

/* Reverse every other word in a given string, then return the string. 
Throw away any leading or trailing whitespace, 
while ensuring there is exactly one space between each word. 
Punctuation marks should be treated as if they are apart of the word in this kata. */

// function reverse(str) {
//     let s = str.split(' ')
//     let res = []
//     for (let i = 0; i < s.length; i++) {
//         if (i % 2 == 0) res.push(s[i])
//         else res.push([...s[i]].reverse().join(''))
//     }
//     return res.join(' ').trim()
// }

const reverse = str => str.trim().split(' ').map((v, i) => i % 2 ? [...v].reverse().join `` : v).join(' ')


q = reverse("Reverse this string, please!")
// "Reverse siht string, !esaelp"
q
q = reverse("I really don't like reversing strings!")
// "I yllaer don't ekil reversing !sgnirts"
q