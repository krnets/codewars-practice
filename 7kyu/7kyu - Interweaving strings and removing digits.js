// 7kyu - Interweaving strings and removing digits

/* Your friend Rick is trying to send you a message, but he is concerned that it would get intercepted by his partner. 
He came up with a solution:

1) Add digits in random places within the message.
2) Split the resulting message in two. He wrote down every second character on one page, and the remaining ones on another. 
He then dispatched the two messages separately.

Write a function interweave(s1, s2) that reverses this operation to decode his message!

Example 1: interweave("hlo", "el") -> "hello" 
Example 2: interweave("h3lo", "el4") -> "hello"

Rick's a bit peculiar about his formats. He would feel ashamed if he found out his message led to extra white spaces 
hanging around the edges of his message... */

// function interweave(s1, s2) {
//     let arr = []
//     let len = (s1 + s2).length
//     s1 = [...s1]
//     s2 = [...s2]
//     for (let i = 0; i < len; i++) {
//         if (i % 2 == 0)
//             arr.push(s1.shift())
//         else
//             arr.push(s2.shift())
//     }
//     return arr.join('').replace(/\d/g, '')
// }

// const interweave = (s1, s2) => [...Array(s1.length)].map((_, i) => s1[i] + (s2[i] || '')).join('').replace(/\d/g, '')
// const interweave = (s1, s2) => [...s1].map((_, i) => s1[i] + (s2[i] || '')).join('').replace(/\d/g, '')

const clean = string => string.replace(/[0-9]/g, '')
const zipper = (a, b) => [...a].map((letter, index) => letter + (b[index] || ''))
const zip = strings => strings.reduce(zipper).join('')
const interweave = (...strings) => clean(zip(strings))

q = interweave("", "") // ""
q
q = interweave("hlo", "el") // 'hello'
q
q = interweave("h3lo", "el4") // 'hello'
q