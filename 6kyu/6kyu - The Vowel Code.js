// 6kyu - The Vowel Code

// const encode = string => string.replace(/[aeiou]/g, c => '12345' ['aeiou'.indexOf(c)])
// const decode = string => string.replace(/[12345]/g, c => 'aeiou' ['12345'.indexOf(c)])

// const encode = string => string.replace(/a|e|i|o|u/g, matched => 'aeiou'.indexOf(matched) + 1)
// const decode = string => string.replace(/1|2|3|4|5/g, matched => 'aeiou'.charAt(matched - 1))

const encode = string => string.replace(/[aeiou]/g, c => 'aeiou'.indexOf(c) + 1)
const decode = string => string.replace(/[12345]/g, c => 'aeiou'.charAt(c - 1))


q = encode("hello") // 'h2ll4'
q
q = decode("h3 th2r2") // 'hi there'
q
q = encode('How are you today?') // 'H4w 1r2 y45 t4d1y?'
q
q = encode('This is an encoding test.') // 'Th3s 3s 1n 2nc4d3ng t2st.'
q
q = decode('h2ll4') // 'hello'
q
q = decode(encode('hello')) // 'hello'
q