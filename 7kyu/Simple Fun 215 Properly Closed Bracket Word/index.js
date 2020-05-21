// 7kyu - Simple Fun 215 Properly Closed Bracket Word

/* We call letter x a counterpart of letter y, if x is the ith letter of the English alphabet, 
and y is the (27 - i)th for each valid i (1-based). 
For example, 'z' is the counterpart of 'a' and vice versa, 'y' is the counterpart of 'b', and so on.

A properly closed bracket word (PCBW) is such a word that its first letter is the counterpart of its last letter, 
its second letter is the counterpart of its last by one letter, and so on.

Determine if the given word is a PCBW or not.
Input/Output

    [input] string word
    A string consisting of lowercase letters.
    0 < word.length ≤ 30

    [output] a boolean value
    true if word is a PCBW, false otherwise.

For word = "abiryz", the output should be true.
'a' is the counterpart of 'z';
'b' <-> 'y'
'i' <-> 'r'

// A ..... Z
// 0 ..... 26

// A <-> Z  0 <-> 26
// B <-> Y  1 <-> 25
// C <-> X  2 <-> 24
// D <-> W  3 <-> 23

For word = "abitryz", the output should be false. */

// function closedBracketWord(word) {
//     let abc = [...Array(26).keys()].map(v => String.fromCharCode(v + 97))
//     let xyz = abc.slice().reverse()
//     let lastHalfRev = word.slice(word.length / 2).split('').reverse().join('')

//     for (let i = 0; i < word.length / 2; i++)
//         if (abc.indexOf(word[i]) != xyz.indexOf(lastHalfRev[i]))
//             return false
//     return true

function closedBracketWord(word) {
    let start = 'a'.charCodeAt()
    let abc = [...Array(26).keys()].map(v => String.fromCharCode(v + start))
    let xyz = abc.slice().reverse()

    for (let i = 0; i < word.length; i++)
        if (abc.indexOf(word[i]) != xyz.indexOf(word[word.length - i - 1]))
            return false
    return true
}

// const closedBracketWord = word => word == [...word].reverse().map(c => 'abcdefghijklmnopqrstuvwxyz' ['zyxwvutsrqponmlkjihgfedcba'.indexOf(c)]).join('')

// const closedBracketWord = (word) => [...word].every((_, i) => word.charCodeAt(i) + word.charCodeAt([word.length - i - 1]) == 219)

q = closedBracketWord("abiryz") // true
q
q = closedBracketWord("aibryz") // false
q
q = closedBracketWord("abitryz") // false
q
q = closedBracketWord("zhuazfsa") // true
q
q = closedBracketWord("baby") // false
q
q = closedBracketWord("grit") // true
q
q = closedBracketWord("foul") // false
q