// 7kyu - Password maker

/* One suggestion to build a satisfactory password is to start with a memorable phrase or sentence 
and make a password by extracting the first letter of each word.

Even better is to replace some of those letters with numbers (e.g., the letter O can be replaced with the number 0):

    instead of including i or I put the number 1 in the password;
    instead of including o or O put the number 0 in the password;
    instead of including s or S put the number 5 in the password.

"Give me liberty or give me death"  --> "Gml0gmd"
"Keep Calm and Carry On"            --> "KCaC0" */

// const makePassword = phrase => phrase.split(' ').map(v => v[0]).join('').replace(/[ios]/gi, m => /i/i.test(m) ? 1 : /o/i.test(m) ? 0 : 5)

const makePassword = phrase => phrase.split(' ').map(v => v[0]).join('').replace(/i/gi, 1).replace(/o/gi, 0).replace(/s/gi, 5)

// const makePassword = (phrase, d = { i: 1, o: 0, s: 5 }) => phrase.replace(/\b(\w)\w+(\W|$)/g, (a, b, c) => d[b.toLowerCase()] || b)


q = makePassword("Give me liberty or give me death"), "Gml0gmd", "Wrong output for 'Give me liberty or give me death'"
q
q = makePassword("Keep Calm and Carry On"), "KCaC0", "Wrong output for 'Keep Calm and Carry On'"
q