// 8kyu - Is there a vowel in there?

/* Given an array of numbers, check if any of the numbers are the character codes for lower case vowels (a, e, i, o, u).
If they are, change the array value to a string of that vowel.
Return the resulting array. */

// function isVow(arr) {
//     return arr.map(v => 'aeiou'.includes(String.fromCharCode(v)) ? String.fromCharCode(v) : v)
// }

// function isVow(arr) {
//     let res = []
//     for (let i = 0; i < arr.length; i++) {
//         let cmp = String.fromCharCode(arr[i])
//         res.push('aeiou'.includes(cmp) ? cmp : arr[i])
//     }
//     return res
// }

function isVow(arr) {
    for (let i = 0; i < arr.length; i++) {
        let cmp = String.fromCharCode(arr[i])
        if ('aeiou'.includes(cmp))
            arr[i] = cmp
    }
    return arr
}

q = isVow([118, 117, 120, 121, 117, 98, 122, 97, 120, 106, 104, 116, 113, 114, 113, 120, 106])
// [118,"u",120,121,"u",98,122,"a",120,106,104,116,113,114,113,120,106]
q
q = isVow([101, 121, 110, 113, 113, 103, 121, 121, 101, 107, 103])
// ["e",121,110,113,113,103,121,121,"e",107,103]
q