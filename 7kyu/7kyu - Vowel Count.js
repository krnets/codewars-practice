// const countVowels = str => [...str].map(v => /[aeiou]/.test(v)).reduce((a, b) => a + b, 0)
const countVowels = str => (str.match(/[aeiou]/gi) || []).length
// const countVowels = str => str.replace(/[^aeiou]/gi, '').length

q = countVowels("abracadabra") // 5
q
q = countVowels("brhms") // 5
q