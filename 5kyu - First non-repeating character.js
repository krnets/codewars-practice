// 5kyu - First non-repeating character

// function firstNonRepeatingLetter(str) {
//     let myArr = [...str].map((v,i) => [...v, {count: 0}])
//     let myMap = new Map(myArr)

//     for (let c of str) {
//         myMap.get(c).count++
//     }

//     for(let c of str) {
//         if (myMap.get(c).count == 1) {
//             return c
//         }
//     }

//     return ''
// }

// function firstNonRepeatingLetter(str) {
//     // let aa = [...str].map(v=>v.toLowerCase())
//     // aa
//     let a = [...str].map(v => v.charCodeAt(0))
//     // let a = [...str].map(v => v.toLowerCase().charCodeAt(0))
//     a
//     // let b = a.filter((v,i,a) => a.indexOf(String.fromCharCode(v).toLowerCase().charAt(0)) == a.lastIndexOf(v))
//     // a.indexOf(v) == a.lastIndexOf(v) || 
//     b
//     let c = b[0]
//     c
//     return String.fromCharCode(c)
// }

// function firstNonRepeatingLetter(str) {
//     let result = ''
//     // let a = /[a-z]/gi.test(str[1])
//     // a
//     for (let i = 0; i < str.length; i++) {
//         // if (/[a-z]/g.test(str[i])) {
//         // result.push(str[i])
//         // }
//         if (/[a-z]/gi.test(str[i]) == false) {
//             return str[i]    
//         }
//         if (str.indexOf(str[i]) === str.lastIndexOf(str[i].toLowerCase())) {
//         // if (str.indexOf(str[i]) === str.lastIndexOf(str[i].toLowerCase()))
//             // result += str[i];
//             // break
//             return str[i]
//         // } else {
//             // return str[i]
//         }

//     }
//     return result
// }

// function firstNonRepeatingLetter(str) {
//     let index = str
//         .toLowerCase()
//         .split('')
//         .findIndex(char => str.indexOf(char) == str.lastIndexOf(char))
//     return index === -1 ? '' : str[index]
// }

// const firstNonRepeatingLetter = s => s[s.toLowerCase()
//                                         .split('')
//                                         .findIndex(letter => s.toLowerCase().split('').filter(l => l === letter).length === 1)] 
//                                         || ''

// const firstNonRepeatingLetter = s => s[[...s.toLowerCase()].findIndex((c, _, s) => s.indexOf(c) === s.lastIndexOf(c))] || '' 

// function firstNonRepeatingLetter(str) {
//     const chars = [...str]
//     const upper = [...str.toUpperCase()]

//     for (let i = 0; i < upper.length; i++) {
//         if (chars[i].charCodeAt(0) < 65 || chars[i].charCodeAt(0) > 122) {
//             if (chars.indexOf(chars[i]) == chars.lastIndexOf(chars[i]))
//                 return chars[i]
//         }
//         if (upper.indexOf(upper[i]) == upper.lastIndexOf(upper[i]))
//             return chars[i];
//     }
//     return ''
// }

// function firstNonRepeatingLetter(str) {
//     for (let i in str) 
//         if (str.match(new RegExp(str[i], "gi")).length === 1)
//             return str[i]
//     return ''
// }

// const firstNonRepeatingLetter = str => [...str].find(c => str.match(new RegExp(`${c}`, 'gi')).length == 1) || ''

function firstNonRepeatingLetter(str) {
    let newStr = str.toLowerCase()
    for (let i = 0; i < newStr.length; i++)
        if (newStr.indexOf(newStr[i]) === newStr.lastIndexOf(newStr[i]))
            return str[i]
    return ''
}

q = firstNonRepeatingLetter(',') // 'a'
q
q = firstNonRepeatingLetter('a') // 'a'
q
q = firstNonRepeatingLetter('stress') // 't'
q
q = firstNonRepeatingLetter('moonmen') // 'e'
q