// 6kyu - Simple ROT13.5 cypher

/* You are asked to write a simple cypher that rotates every character 
(in range [a-zA-Z], special chars will be ignored by the cipher) by 13 chars. 
As an addition to the original ROT13 cipher, this cypher will also cypher numerical digits ([0-9]) with 5 chars.

"The quick brown fox jumps over the 2 lazy dogs"
will be cyphered to:
"Gur dhvpx oebja sbk whzcf bire gur 7 ynml qbtf"

Your task is to write a ROT13.5 (ROT135) method that accepts a string and encrypts it. 
Decrypting is performed by using the same method, but by passing the encrypted string again.

Note: when an empty string is passed, the result is also empty. */


const ROT135 = (input) => input.replace(/\d/g, (d) => (Number(d) + 5) % 10)
    .replace(/[a-z]/g, (c) => String.fromCodePoint((c.charCodeAt() - 97 + 13) % 26 + 97))
    .replace(/[A-Z]/g, (c) => String.fromCodePoint((c.charCodeAt() - 65 + 13) % 26 + 65))

// const ROT135 = s => s.replace(/./g, c => "nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM5678901234" 
// ["abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789".indexOf(c)] || c);

// function ROT135(input) {
//     const abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
//     const nop = "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm5678901234"
//     return input.replace(/[A-Za-z0-9]/g, c => nop[abc.indexOf(c)])
// }

// 97 - 122
q = ROT135("abc xyz")
q
q = ROT135("The quick brown fox jumps over the 2 lazy dogs")
// "Gur dhvpx oebja sbk whzcf bire gur 7 ynml qbtf"
q
q = ROT135("Gur dhvpx oebja sbk whzcf bire gur 7 ynml qbtf")
// "The quick brown fox jumps over the 2 lazy dogs"
q