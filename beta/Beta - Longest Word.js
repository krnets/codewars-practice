// Beta - Longest Word

// Write a function that returns the longest word in a sentence

// function theLongest(text) {
//     let a = text.split(' ')
//     let b = a.map((v, i) => [v.length, i]).sort((a, b) => b[0] - a[0])[0][1]
//     return a[b]
// }

// function theLongest(text) {
//     let a = text.split(' ')
//     let b = a.map((v, i) => [v.length, i])
//     let c = b.reduce((acc, v) => Math.max(acc, v[0]), 0)
//     let d = b.find(v => v[0] == c)
//     return a[d[1]]
// }

// function theLongest(text) {
//     let a = text.split(' ')
//     return a[a.map((v, i) => [v.length, i]).sort((a, b) => b[0] - a[0])[0][1]]
// }

// const theLongest = (text) => (arr = text.split(' '), arr[arr.map((v, i) => [v.length, i]).sort((a, b) => b[0] - a[0])[0][1]])

const theLongest = (text) => text.split(' ').sort((a, b) => b.length - a.length)[0]

q = theLongest("Write a function that returns the longest word in a sentence")
q