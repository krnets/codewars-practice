// 7kyu - Reverse words

// const reverseWords = str => str.split(' ').map(v => [...v].reverse().join ``).join(' ')
// const reverseWords = str => str.split('').reverse().join('').split(' ').reverse().join(' ')
const reverseWords = str => str.replace(/\S+/g, v => [...v].reverse().join ``)

q = reverseWords('The quick brown fox jumps over the lazy dog.')
// 'ehT kciuq nworb xof spmuj revo eht yzal .god'
q
q = reverseWords('apple')
// 'elppa'
q
q = reverseWords('a b c d')
// 'a b c d'
q
q = reverseWords('double  spaced  words')
// 'elbuod  decaps  sdrow'
q