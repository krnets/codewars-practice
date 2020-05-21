// 6kyu - Alphabetized

/* Re-order the characters of a string, so that they are concatenated into a new string in 
"case-insensitively-alphabetical-order-of-appearance" order. Whitespace and punctuation shall simply be removed!

The input is restricted to contain no numerals and only words containing the english alphabet letters. */

function alphabetized(s) {
    let res = ''
    for (let i = 'a'.charCodeAt(); i < 'a'.charCodeAt() + 26; i++)
        for (let j = 0; j < s.length; j++)
            if (s[j].toLowerCase().charCodeAt() == i)
                res += s[j]
    return res
}

// const alphabetized = s =>"abcdefghijklmnopqrstuvwxyz".split('').map(e=> (s.match(new RegExp(e,"gi"))||[]  ).join('') ).join('')

// const alphabetized = (s) => [...'a'.repeat(26).replace(/./g, (_, i) => String.fromCharCode(i + 97))].map(v => (s.match(new RegExp(v, 'gi')) || []).join('')).join('')



q = alphabetized('The Holy Bible') // 'BbeehHilloTy'
q