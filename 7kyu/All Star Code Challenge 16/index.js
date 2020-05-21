// 7kyu - All Star Code Challenge 16

/* Create a function called noRepeat() that takes a string argument and returns a single letter string of 
the first not repeated character in the entire string.

noRepeat("aabbccdde") // => "e"
noRepeat("wxyz") // => "w"
noRepeat("testing") // => "e"

Note: ONLY letters from the english alphabet will be used as input There will ALWAYS be at least one 
non-repeating letter in the input string */

// function noRepeat(str) {
//     let charMap = {};
//     [...str].forEach(v => charMap[v] = ++charMap[v] || 1)
//     for (let i = 0; i < str.length; i++)
//         if (charMap[str[i]] == 1)
//             return str[i]
//     return charMap
// }

function noRepeat(str) {
    for (let ch of str)
        if (str.split(ch).length == 2)
            return ch
}

q = noRepeat('aabbccdde') // "e"
q
q = noRepeat('wxyz') // "w"
q
q = noRepeat('testing') // "e"
q