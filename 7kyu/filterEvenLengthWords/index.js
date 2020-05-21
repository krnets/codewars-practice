// 7kyu - filterEvenLengthWords

/* Given an array of strings, "filterEvenLengthWords" returns an array containing only the elements 
of the given array whose length is an even number.

var output = filterEvenLengthWords(['word', 'words', 'word', 'words']) // --> ['word', 'word'] */

const filterEvenLengthWords = words => words.filter(v => v.length % 2 == 0)

q = filterEvenLengthWords(['Hello', 'World']).length // 0
q
q = filterEvenLengthWords(['One', 'Two', 'Three', 'Four']).length // 1
q