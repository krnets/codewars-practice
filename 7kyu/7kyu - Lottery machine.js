// 7kyu - Lottery machine

/* Your task is to write an update for a lottery machine. 
Its current version produces a sequence of random letters and integers (passed as a string to the function lottery()). 
Your code inside lottery() must filter out all letters and return unique integers as a string. 
If there are no integers in the string return - “One more run!”. */

// const lottery = (str) => [...str].filter((v, i, a) => /\d/.test(v) && a.indexOf(v) == i).join('') || 'One more run!'
// const lottery = (str) => [...str].filter((v, i, a) => /\d/.test(v) && a.indexOf(v) == i).join('') || 'One more run!'
const lottery = (str) => [...new Set(str.replace(/\D/g, ''))].join('') || 'One more run!'

q = lottery("wQ8Hy0y5m5oshQPeRCkG") // "805", "should return unique integer(s) or a string"
q
q = lottery("ffaQtaRFKeGIIBIcSJtg") // "One more run!", "should return unique integer(s) or a string"
q