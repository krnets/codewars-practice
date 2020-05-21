// 7kyu - The old switcheroo

/* Write a function 

vowel2index(str) 

that takes in a string and replaces all the vowels [a,e,i,o,u] with their respective positions within that string. <br/>

vowel2index('this is my string') == 'th3s 6s my str15ng'
vowel2index('Codewars is the best site in the world') == 'C2d4w6rs 10s th15 b18st s23t25 27n th32 w35rld'
vowel2index('') == ''

Your function should be case insensitive to the vowels. */

// const vowel2index = (str) => [...str].map((v, i) => /[aeiou]/i.test(v) ? i + 1 : v).join('')
const vowel2index = (str) => str.replace(/[aeiou]/gi, (_, i) => i + 1)

q = vowel2index('this is my string') // 'th3s 6s my str15ng'
q
q = vowel2index('Codewars is the best site in the world') // 'C2d4w6rs 10s th15 b18st s23t25 27n th32 w35rld'
q
q = vowel2index('Tomorrow is going to be raining') // 'T2m4rr7w 10s g1415ng t20 b23 r2627n29ng'
q
q = vowel2index('') // ''
q