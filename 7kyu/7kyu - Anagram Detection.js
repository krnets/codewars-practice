// 7kyu - Anagram Detection

/* An anagram is the result of rearranging the letters of a word to produce a new word (see wikipedia).
Anagrams are case insensitive
Complete the function to return true if the two arguments given are anagrams of each other; return false otherwise.

    "foefet" is an anagram of "toffee"
    "Buckethead" is an anagram of "DeathCubeK" */

// const isAnagram = (test, original) => [...test.toLowerCase()].sort().join `` == [...original.toLowerCase()].sort().join ``
// const isAnagram = (test, original) => (s => s(test) == s(original))(r => r.toLowerCase().split ``.sort().join ``)
const isAnagram = (test, original) => (s => s(test) == s(original))(r => [...r.toLowerCase()].sort().join ``)

q = isAnagram("foefet", "toffee") // true, 'The word foefet is an anagram of toffee'
q
q = isAnagram("Buckethead", "DeathCubeK") // true, 'The word Buckethead is an anagram of DeathCubeK'
q
q = isAnagram("Twoo", "WooT") // true, 'The word Twoo is an anagram of WooT'
q
q = isAnagram("dumble", "bumble") // false, 'Characters do not match for test case dumble, bumble'
q
q = isAnagram("ound", "round") // false, 'Missing characters for test case ound, round'
q
q = isAnagram("apple", "pale") // false, 'Same letters, but different count'
q