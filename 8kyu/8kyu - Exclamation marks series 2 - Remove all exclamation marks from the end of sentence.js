// 8kyu - Exclamation marks series 2 - Remove all exclamation marks from the end of sentence

const remove = (s) => s.replace(/\!+$/, '')

q = remove("Hi!") // "Hi"
q
q = remove("Hi!!!") // "Hi"
q
q = remove("!Hi") // "!Hi"
q
q = remove("!Hi!") // "!Hi"
q
q = remove("Hi! Hi!") // "Hi! Hi"
q
q = remove("Hi") // "Hi"
q