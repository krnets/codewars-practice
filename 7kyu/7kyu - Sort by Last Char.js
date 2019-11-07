// 7kyu - Sort by Last Char

const last = x => x.split(' ').sort((a, b) => a.charCodeAt(a.length - 1) - b.charCodeAt(b.length - 1))
// const last = x => x.split(' ').sort((a, b) => a.slice(-1).localeCompare(b.slice(-1)))


q = last('man i need a taxi up to ubud') // ['a', 'need', 'ubud', 'i', 'taxi', 'man', 'to', 'up']
q
q = last('what time are we climbing up the volcano') // ['time', 'are', 'we', 'the', 'climbing', 'volcano', 'up', 'what']
q
q = last('take me to semynak') // ['take', 'me', 'semynak', 'to']
q