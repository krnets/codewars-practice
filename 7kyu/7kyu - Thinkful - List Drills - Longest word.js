// 7kyu - Thinkful - List Drills: Longest word

/* Complete the function that takes one argument, a list of words, and returns the length of the longest word in the list.

['simple', 'is', 'better', 'than', 'complex'] ==> 7

Do not modify the input list.
Fundamentals | Lists | Data Structures | Loops | Control Flow | Basic Language Features */

// const longest = (words) => words.sort((a, b) => b.length - a.length)[0].length
// const longest = (words) => words.reduce((a, b) => Math.max(a, b.length), 0)
const longest = (words) => Math.max(...words.map(v => v.length))

// function longest(words) {
//     let lengthseen = 0
//     for (const w of words)
//         if (w.length > lengthseen) lengthseen = w.length
//     return lengthseen
// }

q = longest(['simple', 'is', 'better', 'than', 'complex']) // 7
q
q = longest(['explicit', 'is', 'better', 'than', 'implicit']) // 8
q
q = longest(['beautiful', 'is', 'better', 'than', 'ugly']) // 9
q