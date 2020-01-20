// 8kyu - Smallest unused ID

/* Write a method, which returns the smallest unused ID for your next new data item...
The given array of used IDs may be unsorted. For test reasons there may be duplicate IDs, 
but you don't have to find or remove them! */

// function nextId(ids) {
//     let res = Array(Math.max(...ids)).fill().map((_, i) => i).filter(v => !ids.includes(v))
//     return res.length ? res[0] : Math.max(...ids) + 1
// }

// function nextId(ids) {
//     let set = new Set(ids)
//     for (let i = 0; i <= ids.length; i++)
//         if (!set.has(i))
//             return i
// }

// function nextId(ids) {
//     for (let i = 0; i < ids.length; i++)
//         if (ids.indexOf(i) == -1) 
//             return i
//     return ids.length
// }

// const nextId = (ids) => ids.filter((v, _, a) => !a.includes(v + 1)).sort((a, b) => a - b)[0] + 1

function nextId(ids) {
    let x = 0
    while (ids.includes(x)) x++
    return x
}

q = nextId([0, 1, 2, 3, 5]) // 4
q
q = nextId([0, 1, 1, 2, 5, 0, 1, 2, 3, 5]) // 4
q
q = nextId([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) // 11
q