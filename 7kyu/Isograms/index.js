// 7kyu - Isograms

// const isIsogram = str => [...String(str)].filter((v, i, a) => a.indexOf(v) !== a.lastIndexOf(v))
// const isIsogram = str => str.match(/([a-z]).*\1/i)
// const isIsogram = str => !str.match(/([a-z]).*\1/i)
// const isIsogram = str => !/(.).*?\1/i.test(str)
// const isIsogram = str => !str || new Set(str.toLowerCase()).size == str.length
// const isIsogram = str => !str || [...str.toLowerCase()].every((v, i, arr) => arr.indexOf(v) == i)

// function isIsogram(str) {
//     if (typeof str != 'string') return undefined
//     str = str.toLowerCase()
//     for (let i = 0; i < str.length; i++)
//         for (let j = i + 1; j < str.length; j++)
//             if (str[i] == str[j])
//                 return false
//     return true
// }

// function isIsogram(str) {
//     if (typeof str != 'string') return undefined
//     str = str.toLowerCase()
//     for (let i = 0; i < str.length; i++)
//         if (str.indexOf(str.charAt(i), i+1) >= 0)
//             return false
//     return true
// }

// function isIsogram(str) {
//     if (typeof str != 'string') return undefined
//     str = str.toLowerCase().split('').sort()
//     for (let i = 0; i < str.length - 1; i++)
//         if (str[i] == str[i + 1])
//             return false
//     return true
// }

// function isIsogram(str) {
//     if (typeof str != 'string') return undefined
//     return str.toLowerCase().split('').sort().filter((v, i, a) => v == a[i + 1]).length == 0
// }

// const isIsogram = str => !str || str.toLowerCase().split('').sort().filter((v, i, a) => v == a[i + 1]).length == 0
// const isIsogram = str => !str || new Set(str.toUpperCase()).size == str.length
const isIsogram = str => new Set(str.toUpperCase()).size == str.length
// const isIsogram = str => String(str) !== str ? 'not a string' : new Set(str.toUpperCase()).size == str.length

q = isIsogram("Dermatoglyphics") // true
q
q = isIsogram("isogram") // true
q
q = isIsogram("aba") // false, "same chars may not be adjacent"
q
q = isIsogram("moOse") // false, "same chars may not be same case"
q
q = isIsogram("isIsogram") // false
q
q = isIsogram("") // true, "an empty string is a valid isogram"
q