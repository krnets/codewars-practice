// 7kyu - Jenny the youngest detective

/* Jenny is 9 years old. She is the youngest detective in North America. Jenny is a 3rd grader student, 
so when a new mission comes up, she gets a code to decipher in a form of a sticker (with numbers) in her 
math notebook and a comment (a sentence) in her writing notebook. All she needs to do is to figure out one word, 
from there she already knows what to do. And here comes your role - you can help Jenny find out what the word is!

In order to find out what the word is, you should use the sticker (array of 3 numbers) to retrieve 3 letters 
from the comment (string) that create the word.

    Each of the numbers in the array refers to the position of a letter in the string, in increasing order.
    Spaces are not places, you need the actual letters. No spaces.
    The returned word should be all lowercase letters.
    if you can't find one of the letters using the index numbers, return "No mission today". 

Example: input: [5, 0, 3], "I Love You" output: "ivy" (0 = "i", 3 = "v", 5 = "y") */

// function missingWord(nums, str) {
//     str = str.replace(/\s/g, '')
//     let out = ''
//     let sorted = nums.sort((a, b) => a - b)
//     for (let i = 0; i < sorted.length; i++) {
//         if (str[sorted[i]]) out += str[sorted[i]]
//         else return 'No mission today'
//     }
//     return out.toLowerCase()
// }

function missingWord(nums, str) {
    let s = str.toLowerCase().replace(/\W/g, '')
    let r = nums.sort((a, b) => a - b).map(v => s[v]).join('')
    return r.length == nums.length ? r : 'No mission today'
}

q = missingWord([5, 0, 3], "I love you") // "ivy"
q
q = missingWord([29, 31, 8], "The quick brown fox jumps over the lazy dog") // "bay"
q
q = missingWord([12, 4, 6], "Good Morning") // "No mission today"
q