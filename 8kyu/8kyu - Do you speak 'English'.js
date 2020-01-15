// 8kyu - Do you speak "English"?

/* Given a string of arbitrary length with any ascii characters. 
Write a function to determine whether the string contains the whole word "English".

The order of characters is important -- a string "abcEnglishdef" is correct but "abcnEglishsef" is not correct.
Upper or lower case letter does not matter -- "eNglisH" is also correct.
Return value as boolean values, true for the string to contains "English", false for it does not. */

// function spEng(sentence) {
//     return /english/i.test(sentence)
// }

function spEng(sentence) {
    let match = 'english'
    let cmp = sentence.toLowerCase()
    for (var i = 0, j = 0; i < cmp.length; i++)
        if (cmp[i] == match[j])
            j++
    return j == match.length
}


q = spEng("english") // true
q
q = spEng("egnlish") // false
q
q = spEng("abcEnglishdef") // true
q
q = spEng("abcnEglishsef") // false
q