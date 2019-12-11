// 5kyu - Caesar Cipher Helper

/* Write a class that, when given a string, will return an uppercase string with each letter 
shifted forward in the alphabet by however many spots the cipher was initialized to.

If something in the string is not in the alphabet (e.g. punctuation, spaces), simply leave it as is.
The shift will always be in range of [1, 26].

Algorithms | Ciphers | Cryptography | Security | Objects | Classes | Basic Language Features | Object-oriented Programming | Fundamentals | Strings */

// class CaesarCipher {
//     constructor(shift) {
//         this.n = shift;
//     }
//     encode(str) {
//         return [...str.toUpperCase()].map(v => /[A-Z]/.test(v) ? String.fromCharCode((v.charCodeAt() - 65 + this.n) % 26 + 65) : v).join('');
//     }
//     decode(str) {
//         return [...str.toUpperCase()].map(v => /[A-Z]/.test(v) ? String.fromCharCode((v.charCodeAt() + 65 - this.n) % 26 + 65) : v).join('');
//     }
// }

// var CaesarCipher = function (shift) {
//     this.encode = (str) => str.replace(/[a-z]/gi, (c) => String.fromCharCode((c.toUpperCase().charCodeAt(0) + shift - 65) % 26 + 65));
//     this.decode = (str) => str.replace(/[a-z]/gi, (c) => String.fromCharCode((c.toUpperCase().charCodeAt(0) + 26 - shift - 65) % 26 + 65));
// };

// var CaesarCipher = function (shift) {
//     this.encode = (str) => [...str.toUpperCase()].map(v => /[A-Z]/.test(v) ? String.fromCharCode((v.charCodeAt() - 65 + shift) % 26 + 65) : v).join('');
//     this.decode = (str) => [...str.toUpperCase()].map(v => /[A-Z]/.test(v) ? String.fromCharCode((v.charCodeAt() + 65 - shift) % 26 + 65) : v).join('');
// }

// var CaesarCipher = function (shift) {
//     this.encode = (str) => str.toUpperCase().replace(/[A-Z]/g, (c) => String.fromCharCode((c.charCodeAt() - 65 + shift) % 26 + 65))
//     this.decode = (str) => str.toUpperCase().replace(/[A-Z]/g, (c) => String.fromCharCode((c.charCodeAt() + 65 - shift) % 26 + 65))
// }

// var CaesarCipher = function (shift) {
//     let a = 'A'.charCodeAt()
//     this.encode = (str) => str.toUpperCase().replace(/[A-Z]/g, (c) => String.fromCharCode((c.charCodeAt() + shift + a) % 26 + a))
//     this.decode = (str) => str.toUpperCase().replace(/[A-Z]/g, (c) => String.fromCharCode((c.charCodeAt() - shift + a) % 26 + a))
// }

var CaesarCipher = function (shift) {
    let a = 'A'.charCodeAt()
    this.encode = (str) => str.toUpperCase().replace(/[A-Z]/g, (c) => String.fromCharCode((c.charCodeAt() + a + shift) % 26 + a))
    this.decode = (str) => str.toUpperCase().replace(/[A-Z]/g, (c) => String.fromCharCode((c.charCodeAt() + a - shift) % 26 + a))
}


var c = new CaesarCipher(5); // creates a CipherHelper with a shift of five
q = c.encode('Codewars'); // returns 'HTIJBFWX'
q
q = c.decode('BFKKQJX'); // returns 'WAFFLES'
q