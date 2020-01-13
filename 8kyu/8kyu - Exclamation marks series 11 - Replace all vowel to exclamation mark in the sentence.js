// 8kyu - Exclamation marks series 11 - Replace all vowel to exclamation mark in the sentence

// Replace all vowel to exclamation mark in the sentence. aeiouAEIOU is vowel.

const replace = (s) => s.replace(/[aeiou]/gi, '!')

q = replace("Hi!") // "H!!"
q
q = replace("!Hi! Hi!") // "!H!! H!!"
q
q = replace("aeiou") // "!!!!!"
q
q = replace("ABCDE") // "!BCD!"
q