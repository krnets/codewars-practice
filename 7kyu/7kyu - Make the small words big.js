// 7kyu - Make the small words big!

/* Life isn't always easy as a small word amongst big words. If only they had a code warrior to help them out...

Your task is to make all words which are 3 characters or less into capitals. 
You should also remove any vowels from 'long' (4 characters or more) words.

"The quick brown fox jumps over the lazy dog"
Should become:
"THE qck brwn FOX jmps vr THE lzy DOG"

For the purposes of this kata, mid-word punctuation counts towards the character limit of a word.
e.g: "it's / I'm" should become: "t's / I'M" */

const smallWordHelper = (sentence) => sentence.split(' ').map(v => v.length < 4 ? v.toUpperCase() : v.replace(/[aeiou]/gi, '')).join(' ')


q = smallWordHelper("The quick brown fox jumps over the lazy dog")
//   "THE qck brwn FOX jmps vr THE lzy DOG"
q

q = smallWordHelper("I'm just a small word from a small word family")
//   "I'M jst A smll wrd frm A smll wrd fmly"
q