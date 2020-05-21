// 7kyu - Spot the Differences

/* This kata is part of the collection Mary's Puzzle Books.
Mary brought home a "spot the differences" book. The book is full of a bunch of problems, and each problem consists of two strings that are similar. However, in each string there are a few characters that are different. An example puzzle from her book is:

String 1: "abcdefg"
String 2: "abcqetg"

Notice how the "d" from String 1 has become a "q" in String 2, and "f" from String 1 has become a "t" in String 2.

Write a program spot_diff/Spot that will compare the two strings and 
return a list with the positions where the two strings differ. 
In the example above, your program should return [3, 5] because String 1 is different from String 2 at positions 3 and 5.

• If both strings are the same, return []
• Both strings will always be the same length
• Capitalization and punctuation matter */

// function spot(s1, s2) {
//     for (var res = [], i = 0; i < s1.length; i++)
//         if (s1[i] != s2[i])
//             res.push(i)
//     return res
// }
// const spot = (s1, s2) => [...s1].reduce((res, v, i) => { if (v != s2[i]) res.push(i); return res }, [])
// const spot = (s1, s2) => [...s1].reduce((res, v, i) => { (v != s2[i]) && res.push(i); return res }, [])
const spot = (s1, s2) => [...s1].reduce((res, v, i) => (v != s2[i] ? res.push(i) : null, res), [])
// const spot = (s1, s2) => [...s1].reduce((res, v, i) => v !== s2[i] ? res.concat(i) : res, [])

q = spot('abcdefg', 'abcqetg'), [3, 5], 'Whoops!'
q
q = spot('Hello World!', 'hello world.'), [0, 6, 11], 'Capitalization and punctuation matter!'
q
q = spot('FixedGrey', 'FixedGrey'), [], 'Should return [] if the strings are the same!'
q