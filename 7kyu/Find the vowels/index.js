// 7kyu - Find the vowels

/* We want to know the index of the vowels in a given word, for example, there are two vowels in the word super (the second and fourth letters).

So given a string "super", we should return a list of [2, 4].

Some examples:
Mmmm  => []
Super => [2,4]
Apple => [1,5]
YoMama -> [1,2,4,6]

*NOTE: Vowels in this context refers to English Language Vowels - a e i o u y *

NOTE: this is indexed from [1..n] (not zero indexed!) */

// const vowelIndices = word => [...word].map((c, i) => /[aeiouy]/i.test(c) ? i + 1 : 0).filter(v => v)
const vowelIndices = word => [...word].map((c, i) => /[aeiouy]/i.test(c) && ++i).filter(v => v)
// const vowelIndices = word => [...word].map((c, i) => ~'aeiouyAEIOUY'.indexOf(c) && ++i).filter(Boolean)

// const vowelIndices = word => [...word].reduce((ac, cur, i) => /[aeiouy]/i.test(cur) ? [...ac, i + 1] : ac, [])
// const vowelIndices = word => [...word].reduce((r, e, i) => r.concat(/[aeiouy]/i.test(e) ? ++i : []), [])
// const vowelIndices = word => [...word].reduce((r, e, i) => r.concat(/[aeiouy]/i.test(e) ? ++i : []), [])

// const vowelIndices = (word, a = []) => (word.replace(/[aeiouy]/gi, (m, i) => (a.push(i + 1), m)), a)


q = vowelIndices("muIYXmlIUTSFIzpXOxueSiAPsciqr") // [2, 3, 4, 8, 9, 13, 17, 19, 20, 22, 23, 27]
q
q = vowelIndices("mmm") // []
q
q = vowelIndices("apple") // [1,5]
q
q = vowelIndices("super") // [2,4]
q
q = vowelIndices("orange") // [1,3,6]
q
q = vowelIndices("supercalifragilisticexpialidocious") // [2,4,7,9,12,14,16,19,21,24,25,27,29,31,32,33]
q