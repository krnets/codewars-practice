// 7kyu - Scrolling Text

/* Let's create some scrolling text!

Your task is to complete the function which takes a string, and 
returns an array with all possible rotations of the given string, in uppercase.

scrollingText("codewars") should return:

[ "CODEWARS",
  "ODEWARSC",
  "DEWARSCO",
  "EWARSCOD",
  "WARSCODE",
  "ARSCODEW"
  "RSCODEWA",
  "SCODEWAR" ] */

// function scrollingText(text) {
//     let str = text.toUpperCase()
//     let res = [str]
//     for (let i = 0; i < text.length - 1; i++) {
//         str = str.slice(1) + str.slice(0, 1)
//         res.push(str)
//     }
//     return res
// }

// function scrollingText(text) {
//     let res = []
//     for (let i = 0; i < text.length; i++) {
//         res.push((text.slice(i) + text.slice(0, i)).toUpperCase())
//     }
//     return res
// }

// const scrollingText = text => [...text].map((_, i) => (text.slice(i) + text.slice(0, i)).toUpperCase())
const scrollingText = (t, s = t.toUpperCase()) => [...s].map((_, i) => s.slice(i) + s.slice(0, i))

q = scrollingText('abc') // ["ABC","BCA","CAB"]
q
q = scrollingText('codewars') // [ "CODEWARS", "ODEWARSC", "DEWARSCO", "EWARSCOD", "WARSCODE", "ARSCODEW", "RSCODEWA", "SCODEWAR" ] */
q
