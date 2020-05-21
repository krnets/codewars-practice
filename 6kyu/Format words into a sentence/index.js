// 6kyu - Format words into a sentence

/* Complete the method so that it formats the words into a single comma separated value. 
The last word should be separated by the word 'and' instead of a comma. 
The method takes in an array of strings and returns a single formatted string. 
Empty string values should be ignored. Empty arrays or null/nil values being passed 
into the method should result in an empty string being returned. */

// function formatWords(words) {
//     if (!words) return ''
//     words = words.filter(v => v)
//     switch (words.length) {
//         case 1: return words[0]
//         case 2: return words.join ` and `
//         case 3: return words[0] + ', ' + words[1] + ' and ' + words[2]
//         case 4: return words[0] + ', ' + words[1] + ', ' + words[2] + ' and ' + words[3]
//         default: return ''
//     }
// }

const formatWords = words => (words || []).filter(v => v).join(', ').replace(/,(?= [^,]*$)/, ' and')
// const formatWords = words => words ? words.filter(v => v).join(', ').replace(/,(?= [^,]*$)/, ' and') : ''
// const formatWords = words => words ? words.filter(v => v).join(', ').replace(/(, )+(\S+)$/, ' and $2') : ''
// const formatWords = words => (words || []).filter(v => v).join(', ').replace(/(, )+(\S+)$/, ' and $2')
// const formatWords = words => (words || []).filter(v => v).join(', ').replace(/, ([^,]+)$/, ' and $1')
// const formatWords = words => (words || []).filter(v => v).join(', ').replace(/,(?=\s\w+$)/, ' and')

q = formatWords(['ninja', 'samurai', 'ronin']) // should return "ninja, samurai and ronin"
q
q = formatWords(['ninja', '', 'ronin']) // should return "ninja and ronin"
q
q = formatWords([]) // should return ""
q
q = formatWords(['', '', 'three'])
q
q = formatWords(['one'])
q