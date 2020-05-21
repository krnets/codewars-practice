// 5kyu - Scramblies

/* Complete the function scramble(str1, str2) that returns true if a portion of str1 characters can be 
rearranged to match str2, otherwise returns false.

Notes:

    Only lower case letters will be used (a-z). No punctuation or digits will be included.
    Performance needs to be considered

Input strings s1 and s2 are null terminated.

Examples

scramble('rkqodlw', 'world') ==> True
scramble('cedewaraaossoqqyt', 'codewars') ==> True
scramble('katas', 'steak') ==> False */

function scramble(str1, str2) {
    let charCount1 = {};
    [...str1].forEach(v => charCount1[v] = ++charCount1[v] || 1);
    for (let c of str2) {
        if (!charCount1[c]) {
            return false
        }
        --charCount1[c]
        if (charCount1[c] < 0) {
            return false
        }
    }
    return true
}


q = scramble('cedewaraaossoqqyt', 'codewars') // true
q
q = scramble('katas', 'steak') // false
q
q = scramble('scriptjava', 'javascript') // true
q
q = scramble('scriptingjava', 'javascript') // true
q
q = scramble('scriptsjava', 'javascripts') // true
q
q = scramble('jscripts', 'javascript') // false
q
q = scramble('aabbcamaomsccdd', 'commas') // true
q