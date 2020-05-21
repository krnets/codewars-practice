// Beta - Count the Number of Words in a Sentence

/* Write a function that takes as an input a string of words, and returns the number of words in that string.

str = "Houston, we have a problem"  #  return 5
str = "  Toto, I've got a feeling we're not in Kansas anymore. "  #  return 10 

Contractions (such as "I've", and "we're") count as one word, not two.
Whitespaces at the beginning and end of a string should be ignored. */


// function wordCount(str) {
//     return str.trim().split(' ').length
// }

const wordCount = str => str.trim().split(' ').length


q = wordCount("Everything is hard before it is easy.") // 7
q
q = wordCount(" We are what we repeatedly do; excellence, then, is not an act but a habit.") // 15
q
q = wordCount("May the force be with you. ") // 6
q