// 6kyu - Basic Encryption

/* The most basic encryption method is to map a char to another char by a certain math rule. 
Because every char has an ASCII value, we can manipulate this value with a simple math expression. 
For example 'a' + 1 would give us 'b', because 'a' value is 97 and 'b' value is 98.
You will need to write a method which does exactly that -
get a string as text and an int as the rule of manipulation, and should return encrypted text. for example:

encrypt("a",1) = "b"

Full ascii table is used on our question (256 chars) - so 0-255 are the valid values. */

// const encrypt = (text, rule) => text.replace(/(.)/g, (c) => String.fromCharCode((c.charCodeAt() + rule + 256) % 256))
const encrypt = (text, rule) => text.replace(/./g, c => String.fromCharCode((c.charCodeAt() + rule) % 256))
// const encrypt = (text, rule) => text.replace(/./g, c => String.fromCharCode((c.charCodeAt() + rule) & 255))
// const encrypt = (text, rule) => String.fromCharCode(...[...text].map(c => (c.charCodeAt() + rule) % 256))

q = encrypt("", 1) // "", "text = '', rule = 1"
q
q = encrypt("a", 1) // "b", "text = 'a', rule = 1"
q
q = encrypt("please encrypt me", 2) // "rngcug\"gpet{rv\"og", "text = 'please encrypt me', rule = 2"
q