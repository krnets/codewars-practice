// 7kyu - Exclamation marks series #5: Remove all exclamation marks from the end of words

// Remove all exclamation marks from the end of words. Words are separated by spaces in the sentence.

// const remove = (s) => s.split(' ').map(v => v.replace(/\!+$/, '')).join(' ')

const remove = (s) => s.replace(/\b\!+/g, '')

q = remove('Hi!') // "Hi"
q
q = remove('Hi!!!') // "Hi"
q
q = remove('!Hi') // "!Hi"
q
q = remove('!Hi!') // "!Hi"
q
q = remove('Hi! Hi!') // "Hi Hi"
q
q = remove('!!!Hi !!hi!!! !hi') // "!!!Hi !!hi !hi"
q
