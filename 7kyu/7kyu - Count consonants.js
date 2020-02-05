// 7kyu - Count consonants

/* Write a function consonantCount, consonant_count or ConsonantCount that takes a string of 
English-language text and returns the number of consonants in the string.

Consonants are all letters used to write English excluding the vowels a, e, i, o, u.  */


// function consonantCount(str) {
//     let consonants = Array(26).fill().map((_, i) => String.fromCharCode(i + 65)).join('').replace(/[aeiou]/gi, '')
//     // let consonants = Array(26).fill().map((_, i) => String.fromCharCode(i + 65)).join('').replace(/[AEIOU]/g, '')
//     return str.toUpperCase().replace(/./gi, c => consonants.includes(c) ? c : '').length
// }

// const consonantCount = (str) => (str.match(/[b-df-hj-np-tv-z]/gi) || []).length

const consonantCount = (str) => (str.match(/(?![aeiou])[a-z]/gi) || []).length

q = consonantCount('') // 0, 'q =  string'
q
q = consonantCount('aaaaa') // 0, 'q = aaaaa"'
q
q = consonantCount('XaeiouX') // 2, 'q = XaeiouX"'
q
q = consonantCount('Bbbbb') // 5, 'q = Bbbbb"'
q
q = consonantCount('helLo world') // 7, 'q = helLo world"'
q
q = consonantCount('h^$&^#$&^elLo world') // 7, 'q = h^$&^#$&^elLo world"'
q
q = consonantCount('0123456789') // 0, 'q = 0123456789"'
q
q = consonantCount('012345_Cb') // 2, 'q = 012345_Cb"'
q