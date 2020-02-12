// 7kyu - Find twins

/* Agent 47, you have a new task! Among citizens of the city X are hidden 2 dangerous criminal twins. 
Your task is to identify them and eliminate!

Given an array of integers, your task is to find two same numbers and return one of them, 
for example in array [2, 3, 6, 34, 7, 8, 2] answer is 2.

If there are no twins in the city - return None or the equivalent in the language that you are using. */

// function elimination(arr) {
//     let res = Object.entries(arr.reduce((acc, b) => ((acc[b] = ++acc[b] || 1), acc), {})).filter(v => v[1] == 2)
//     return res.length ? +String(res[0][0]) : null
// }

const elimination = arr => arr.filter((v, i) => i != arr.lastIndexOf(v))[0] || null

// function elimination(arr) {
//     let obj = {}
//     for (const n of arr) {
//         if (obj[n]) return n
//         else obj[n] = 1
//     }
//     return null
// }

q = elimination([2, 5, 34, 1, 22, 1]) // 1, "twins are 1s"
q
q = elimination([2, 2, 34, 1, 22]) // 2, "twins are 2s"
q
q = elimination([2, 5, 34, 1, 22]) // null, "There are no twins in the city"
q
