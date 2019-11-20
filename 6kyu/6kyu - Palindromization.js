// 6kyu - Palindromization

function palindromization(element, n) {
    let res = []
    for (let i = 0; res.length < n; i++) {
        res.push(element[i % element.length])
    }
    let pattern = res.join ``
    let halfPoint = Math.floor(pattern.length / 2)
    let mid = pattern[halfPoint]
    let left = pattern.slice(0, halfPoint)
    let right = [...String(left)].reverse().join ``

    return element == '' || n < 2 ? 'Error!' :
        n % 2 ? left + mid + right : left + right
}

// const palindromization = (s, n) => !s || n < 2 ? 'Error!' :
//     (s = s.repeat(n), h = s.slice(0, n / 2), h + (n & 1 ? s[n >> 1] : '') + [...h].reverse().join ``)

// function palindromization(s, n) {
//     if (s == '' || n < 2) return 'Error!'
//     return s.repeat(n).slice(0, Math.floor(n / 2)) + s.repeat(n).slice(0, Math.ceil(n / 2)).split('').reverse().join('')
// }

q = palindromization("123", 2) // "11"
q
q = palindromization("123", 3) // "121"
q
q = palindromization("123", 4) // "1221"
q
q = palindromization("123", 5) // "12321"
q
q = palindromization("123", 6) // "123321"
q
q = palindromization("123", 7) // "1231321"
q
q = palindromization("123", 8) // "12311321"
q
q = palindromization("123", 9) // "123121321"
q
q = palindromization("123", 10) // "1231221321"
q
q = palindromization("", 2) // "Error!"
q
q = palindromization("123", 1) // "Error!"
q