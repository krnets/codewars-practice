// 7kyu - Character Counter

/* You are going to be given a word. 
Your job will be to make sure that each character in that word has the exact same number of occurrences. 
You will return true if it is valid, or false if it is not. */

// function validateWord(s) {
//     let charCount = {};
//     [...s.toLowerCase()].forEach(v => charCount[v] = ++charCount[v] || 1)
//     return Object.entries(charCount).map(v => v[1]).filter((v, _, a) => a.indexOf(v)).length == 0
// }

function validateWord(s) {
    let c = s.toLowerCase()
    c
    let d = new Set(c)
    d
    return c.length % new Set(c).size == 0
}

q = validateWord("abcabc") // true, "The word was: \"abcabc\" \n"
q
q = validateWord("Abcabc") // true, "The word was: \"Abcabc\" \n"
q
q = validateWord("abc123") // true, "The word was: \"abc123\" \n"
q
q = validateWord("abcabcd") // false, "The word was: \"abcabcd\" \n"
q
q = validateWord("abc!abc!") // true, "The word was: \"abc!abc!\" \n"
q
q = validateWord("abc:abc") // false, "The word was: \"abc:abc\" \n"
q