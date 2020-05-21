// 7kyu  - Simple Fun #49: Decipher

/* Consider the following ciphering algorithm:

For each character replace it with its code.
Concatenate all of the obtained numbers.

Given a ciphered string, return the initial one if it is known that it consists only of lowercase letters.

Note: here the character's code means its decimal ASCII code, the numerical representation of a character used 
by most modern programming languages.

For cipher = "10197115121", the output should be "easy".

 charCode('e') = 101, 
 charCode('a') = 97, 
 charCode('s') = 115 
 charCode('y') = 121.

    [input] string cipher: A non-empty string which is guaranteed to be a cipher for some other string of lowercase letters.
    [output] a string   */

// function decipher(cipher) {
//     let res = []
//     for (let i = 0; i < cipher.length;) {
//         if (cipher[i] == '1') {
//             res.push(cipher.slice(i, i + 3))
//             i += 3
//         } else {
//             res.push(cipher.slice(i, i + 2))
//             i += 2
//         }
//     }
//     return res.reduce((s, v) => s + String.fromCharCode(v), '')
// }

// const decipher = (cipher) => cipher.match(/(1\d{2}|9\d)/g).reduce((s, v) => s + String.fromCharCode(v), '')

// const decipher = (cipher) => cipher.replace(/1?../g, v => String.fromCharCode(v))

const decipher = (cipher) => String.fromCharCode(...cipher.match(/1?\d\d/g))

q = decipher("10197115121") // "easy"
q
q = decipher("98") // "b"
q
q = decipher("122") // "z"
q