// 7kyu - Indexed capitalization

/* Given a string and an array of integers representing indices, capitalize all letters at the given indices.

The input will be a lowercase string with no spaces and an array of digits. */

function capitalize(s, arr) {
    let res = [...s]
    arr.map(v => v <= res.length ? res[v] = res[v].toUpperCase() : null)
    return res.join('')
}

// const capitalize = (s, arr) => [...s].map((c, i) => arr.includes(i) ? c.toUpperCase() : c).join('')

q = capitalize("abcdef", [1, 2, 5]) //'aBCdeF'
q
q = capitalize("abcdef", [1, 2, 5, 100]) //'aBCdeF'
q
q = capitalize("codewars", [1, 3, 5, 50]) //'cOdEwArs'
q
q = capitalize("abracadabra", [2, 6, 9, 10]) // 'abRacaDabRA'
q
q = capitalize("codewarriors", [5]) // 'codewArriors'
q
q = capitalize("indexinglessons", [0]) // 'Indexinglessons'
q