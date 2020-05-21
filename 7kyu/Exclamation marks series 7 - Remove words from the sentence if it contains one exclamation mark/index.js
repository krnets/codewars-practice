// 7kyu - Exclamation marks series #7: Remove words from the sentence if it contains one exclamation mark 

/* Remove words from the sentence if it contains one exclamation mark. 
Words are separated by spaces in the sentence. Please remember, one. */

// const remove = (s) => s.split(' ').map(v => v.replace(/(^\w+!$|^!\w+$)/, '')).filter(Boolean).join(' ')
const remove = (s) => s.split(' ').filter(v => v.split('!').length != 2).join(' ')

q = remove("Hi!") // ""
q
q = remove("Hi! Hi!") // ""
q
q = remove("Hi! Hi! Hi!") // ""
q
q = remove("Hi Hi! Hi!") // "Hi"
q
q = remove("Hi! !Hi Hi!") // ""
q
q = remove("Hi! Hi!! Hi!") // "Hi!!"
q
q = remove("Hi! !Hi! Hi!") // "!Hi!"
q