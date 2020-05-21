// 7kyu - Reverse Letters in Sentence 

/* Take a sentence (string) and reverse each word in the sentence. 
Do not reverse the order of the words, just the letters in each word.

If there is punctuation, it should be interpreted as a regular character; no special rules.
If there is spacing before/after the input string, leave them there.

String will not be empty.

"Hi mom" => "iH mom"
" A fun little challenge! " => " A nuf elttil !egnellahc "

Fundamentals | Loops | Control Flow | Basic Language Features | Strings */

// const reverser = (sentence) => sentence.split(' ').map(v => [...v].reverse().join ``).join ` `
const reverser = (sentence) => sentence.replace(/\S+/g, word => [...word].reverse().join ``)


q = reverser("Hi mom"), 'iH mom'
q
q = reverser("friendzone"), 'enozdneirf'
q
q = reverser(" "), ' '
q