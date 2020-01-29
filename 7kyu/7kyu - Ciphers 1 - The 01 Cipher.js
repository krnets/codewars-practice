// 7kyu - Ciphers #1 - The 01 Cipher

/* Cipher looks at the letter, and sees it's index in the alphabet, the alphabet being a-z, if you didn't know. 
If it is odd, it is replaced with 1, if it's even, its replaced with 0. Note that the index should start from 0. 
If letter's index is odd, replaced with 1. If the character isn't a letter, it remains the same. */

// function encode(p) {
//     let abc = { a:0,b:1,c:0,d:1,e:0,f:1,g:0,h:1,i:0,j:1,k:0,l:1,m:0,n:1,o:0,p:1,q:0,r:1,s:0,t:1,u:0,v:1,w:0,x:1,y:0,z:1 }
//     return [...p.toLowerCase()].map(v => abc.hasOwnProperty(v) ? abc[v] : v).join('')
// }


const encode = (plaintext) => plaintext.replace(/[a-z]/gi, c => 1 - c.charCodeAt() % 2)


q = encode("Hello World!") // "10110 00111!"
q