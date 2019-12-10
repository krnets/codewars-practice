// 6kyu - Consonant value

/* Given a lowercase string that has alphabetic characters only and no spaces, 
return the highest value of consonant substrings. Consonants are any letters of the alpahabet except "aeiou".

We shall assign the following values: a = 1, b = 2, c = 3, .... z = 26.

For example, for the word "zodiacs", let's cross out the vowels. We get: "z o d ia cs"

-- The consonant substrings are: "z", "d" and "cs" and the values are z = 26, d = 4 and cs = 3 + 19 = 22. The highest is 26.
solve("zodiacs") = 26

For the word "strength", solve("strength") = 57
-- The consonant substrings are: "str" and "ngth" with values "str" = 19 + 20 + 18 = 57 and "ngth" = 14 + 7 + 20 + 8 = 49. 
The highest is 57.

Fundamentals | Strings */

// const solve = s => Math.max(...s.split(/[aeiou]/).map(v => v ? ([...v].map(x => x.charCodeAt() - 96).reduce((a, b) => a + b)) : 0))
// const solve = s => Math.max(...s.split(/[aeiou]/).map(v => [...v].map(x => x.charCodeAt() - 96).reduce((a, b) => a + b, 0)))
// const solve = s => s.split(/[aeiou]/).reduce((s, n) => Math.max(s, [...n].reduce((a, b) => a + b.charCodeAt() - 96, 0)), 0)
// const solve = s => Math.max(...s.match(/[^aeiou]+/g).map(v => [...v].reduce((s,v) => s + v.charCodeAt() - 96, 0)))

q = solve("zodiacs") // 26
q
q = solve("chruschtschov") // 80
q
q = solve("khrushchev") // 38
q
q = solve("strength") // 57
q
q = solve("catchphrase") // 73
q
q = solve("twelfthstreet") // 103
q
q = solve("mischtschenkoana") // 80
q