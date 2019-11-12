// 7kyu - The Lazy Startup Office

// function binRota(arr) {
//     for (var res = [], i = 0; i < arr.length; i++) {
//         if (i % 2 == 0) res.push(arr[i])
//         else res.push(arr[i].reverse())
//     }
//     return res.reduce((a, b) => a.concat(b), [])
// }

// const binRota = arr => arr.reduce((a, b, i) => (i % 2 == 0) ? a.concat(b) : a.concat(b.reverse()))
// const binRota = arr => arr.reduce((t, c, i) => t.concat(!(i & 1) ? c : c.reverse()), [])
// const binRota = arr => arr.reduce((s, a, i) => s.concat(i % 2 == 1 ? a.reverse() : a), [])
const binRota = arr => arr.reduce((a, b, i) => a.concat(i % 2 == 0 ? b : b.reverse()))

q = binRota([
    ["Bob", "Nora"],
    ["Ruby", "Carl"]
])
// ["Bob","Nora","Carl","Ruby"]
q
q = binRota([
    ["Billy"]
])
// ["Billy"]
q
q = binRota([
    ["Billy", "Nancy"]
])
// ["Billy","Nancy"]
q
q = binRota([
    ["Billy"],
    ["Megan"],
    ["Aki"],
    ["Arun"],
    ["Joy"]
])
// ["Billy", "Megan", "Aki", "Arun","Joy"]
q
q = binRota([
    ["Sam", "Nina", "Tim", "Helen", "Gurpreet", "Edward", "Holly", "Eliza"],
    ["Billy", "Megan", "Aki", "Arun", "Joy", "Anish", "Lee", "Maryan"],
    ["Nick", "Josh", "Pete", "Kavita", "Daisy", "Francesca", "Alfie", "Macy"]
])

// ["Sam","Nina","Tim","Helen", "Gurpreet", "Edward", "Holly", "Eliza","Maryan","Lee","Anish","Joy","Arun","Aki","Megan","Billy","Nick","Josh","Pete","Kavita","Daisy","Francesca","Alfie","Macy"]
q
q = binRota([
    ["Stefan", "Raj", "Marie"],
    ["Alexa", "Amy", "Edward"],
    ["Liz", "Claire", "Juan"],
    ["Dee", "Luke", "Elle"]
])
// ["Stefan","Raj","Marie","Edward","Amy","Alexa","Liz","Claire","Juan","Elle","Luke","Dee"]
q