// Beta - Filter out the vowels

const vowelFilter = letters => letters.filter(v => !'aeiou'.includes(v))
// const vowelFilter = letters => letters.filter(v => /[^aeuio]/.test(v))
// const vowelFilter = letters => letters.filter(v => v.match(/[^aeiou]/))

q = vowelFilter(["i", "s", "e", "a", "w", "e", "m"]) // ["s", "w", "m"]
q
q = vowelFilter(["s", "d", "r", "l", "n"]) // ["s", "d", "r", "l", "n"]
q
q = vowelFilter(["i", "e", "a", "o", "u"]) // []
q