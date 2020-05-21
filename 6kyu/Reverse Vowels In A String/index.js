// 6kyu - Reverse Vowels In A String

/* In this kata, your goal is to write a function which will reverse the vowels in a string. 
Any characters which are not vowels should remain in their original position. 
For simplicity, you can treat the letter y as a consonant, not a vowel. */

// function reverseVowels(str) {
//     let charIndex = [...str].map((v, i) => [v, i])
//     let vowels = charIndex.filter(v => /[aeiou]/i.test(v[0]))
//     let nonvowels = charIndex.filter(v => !/[aeiou]/i.test(v[0]))
//     let vowelIndices = vowels.map(v => v[1]).reverse()
//     let writeNewIndices = vowels.map((v, i) => [v[0], v[1] = vowelIndices[i]])
//     let mergedAndSorted = [...nonvowels, ...writeNewIndices].sort((a, b) => a[1] - b[1])
//     return mergedAndSorted.map(v => v[0]).join('')
// }

const reverseVowels = str => {
    let vowels = str.replace(/[^aeiou]/gi, '').split('');
    return str.replace(/[aeiou]/gi, _ => vowels.pop());
};

q = reverseVowels("Hello!") // "Holle!"
q
q = reverseVowels("Tomatoes") // "Temotaos"
q
q = reverseVowels("Reverse Vowels In A String") // "RivArsI Vewols en e Streng"
q