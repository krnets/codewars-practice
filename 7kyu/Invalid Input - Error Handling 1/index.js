// 7kyu - Invalid Input - Error Handling #1

/* Your task is to implement a function which takes a string as input and return an object containing the 
properties vowels and consonants. The vowels property must contain the total count of vowels {a,e,i,o,u}, 
and the total count of consonants {a,..,z} - {a,e,i,o,u}. Handle invalid input and don't forget to return valid ones.

The input is any random string. You must then discern what are vowels and what are consonants and sum for 
each category their total occurrences in an object. However you could also receive inputs that are not strings. 
If this happens then you must return an object with a vowels and consonants total of 0 because the input was NOT a string. 
Refer to the Example section for a more visual representation of which inputs you could receive and the outputs expected. 

Input: getCount('test')
Output: {vowels:1,consonants:3}

Input: getCount('tEst')
Output: {vowels:1,consonants:3}

Input getCount('    ')
Output: {vowels:0,consonants:0}

Input getCount()
Output: {vowels:0,consonants:0} */

// const getCount = words =>
//     typeof words == 'string'
//         ? { vowels: (words.match(/[aeiou]/gi) || []).length, consonants: (words.match(/[bcdfghjklmnpqrstvwxyz]/gi) || []).length }
//         : { vowels: 0, consonants: 0 }

function getCount(words) {
    let notValid = typeof words != 'string'
    return {
        vowels: notValid ? 0 : words.replace(/[^aeiou]/gi, '').length,
        consonants: notValid ? 0 : words.replace(/[^bcdfghjklmnpqrstvwxyz]/gi, '').length
    }
}

q = getCount('Test') // {vowels:1,consonants:3},'Should return 1 vowel and 3 consonants'
q
q = getCount('Here is some text') // {vowels:6,consonants:8},'Should return 6 vowel and 8 consonants'
q
q = getCount('To be a Codewarrior or not to be') // {vowels:12,consonants:13},'Should return 12 vowel and 13 consonants'
q
q = getCount('To Kata or not to Kata') // {vowels:8,consonants:9},'Should return 8 vowel and 9 consonants'
q
q = getCount('aeiou') // {vowels:5,consonants:0},'Should return 5 vowel and 0 consonants'
q
q = getCount('TEst') // {vowels:1,consonants:3},'Should return 1 vowel and 3 consonants'
q
q = getCount('HEre Is sOme text   ') // {vowels:6,consonants:8},'Should return 6 vowel and 8 consonants'
q
q = getCount() // {vowels:0,consonants:0}, 'Should return 0 vowel and 0 consonants'
q
q = getCount(['To Kata or not to Kata']) // {vowels:0,consonants:0},'Should return 0 vowel and 0 consonants'
q
q = getCount(undefined) // {vowels:0,consonants:0},'Should return 0 vowel and 0 consonants'
q
