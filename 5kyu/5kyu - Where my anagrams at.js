// 5kyu - Where my anagrams at?

/* What is an anagram? Well, two words are anagrams of each other if they both contain the same letters. For example:

'abba' & 'baab' == true
'abba' & 'bbaa' == true
'abba' & 'abbba' == false
'abba' & 'abca' == false

Write a function that will find all the anagrams of a word from a list. 
You will be given two inputs a word and an array with words. 
You should return an array of all the anagrams or an empty array if there are none.  */

function anagrams(word, words) {
    let cmp = [...word].sort().join('')
    return words.filter(v => [...v].sort().join('') == cmp)
}

q = anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) // ['aabb', 'bbaa']
q
q = anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) // ['carer', 'racer']
q
q = anagrams('laser', ['lazing', 'lazy', 'lacer']) // []
q