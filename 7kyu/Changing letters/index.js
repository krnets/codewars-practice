// 7kyu - Changing letters

/* When provided with a String, capitalize all vowels

Input : "Hello World!"
Output : "HEllO WOrld!"

Note: Y is not a vowel in this kata. */

const swap = st => st.replace(/[aeiou]/g, c => c.toUpperCase())

q = swap("HelloWorld!") // "HEllOWOrld!"
q
q = swap("Sunday") // "SUndAy"
q
