// 7kyu - Wordsearch

/* Create a function wordSearch(word,text) that searches to see whether a word word is present in the given text variable.
Note it has to be a full word which means it is surround by a word boundary (spaces, end/start of string, various punctuation, ... ).
Fundamentals | Regular Expressions | Declarative Programming | Advanced Language Features | Strings */

// const wordSearch = (word, text) => !!text.match(new RegExp(`\\b${word}\\b`))
// const wordSearch = (word, text) => text.search('\\b' + word + '\\b') > -1
// const wordSearch = (word, text) => new RegExp(`\\b${word}\\b`).test(text)
const wordSearch = (word, text) => new RegExp('\\b' + word + '\\b').test(text)

const myText = "what makes the desert beautiful, said the little prince is that somewhere it hides a well";

q = wordSearch("desert", myText) // true
q
q = wordSearch("blue", myText) // false
q
q = wordSearch("well", myText) // true
q
q = wordSearch("house", myText) // false
q
q = wordSearch("beautiful", myText) // true
q
q = wordSearch("prince", myText) // true
q
q = wordSearch("le prince", myText) // false
q