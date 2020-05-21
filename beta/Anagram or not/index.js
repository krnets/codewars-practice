// Beta - Anagram or not

/* "Any word or phrase that exactly reproduces the letters in another order is an anagram." (Wikipedia). 
Add numbers to this definition to be more interest.

Examples of anagrams:

William Shakespeare = I am a weakish speller
silent = listen
12345 = 54321

The challenge is to write the function isAnagram to return True if the word test 
is an anagram of the word original and False if not. 

Note: Anagrams are case insensitive, ignore all non-alphanumeric characters, input will always be two strings. 
Also: two identical words may be considered to be an edge case of an anagram, but for this kata they are still correct anagrams. */



// const isAnagram = (test, original) => [...test.toLowerCase().replace(/\W/g, '')].sort().join('') == [...original.toLowerCase().replace(/\W/g, '')].sort().join('')
// const isAnagram = (test, original) => (a = [test, original].map(v => [...v.toLowerCase().replace(/\W/g, '')].sort().join('')))[0] == a[1]
const isAnagram = (test, original) => (f = v => [...v.toLowerCase().replace(/\W/g, '')].sort().join(''), f(test) == f(original))

q = isAnagram("William Shakespeare", "I am a weakish speller") // true
q
q = isAnagram("Silent", "Listen") // true
q
q = isAnagram("Car", "Cat") // false, "Car is not an anagram of Cat"
q
q = isAnagram("12345", "54321") // true
q