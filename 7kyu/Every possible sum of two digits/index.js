// 7kyu - Every possible sum of two digits

/* Given a long number, return all the possible sum of two digits of it.

For example, 12345: all possible sum of two digits from that number are:
[ 1 + 2, 1 + 3, 1 + 4, 1 + 5, 2 + 3, 2 + 4, 2 + 5, 3 + 4, 3 + 5, 4 + 5 ]

Therefore the result must be:
[ 3, 4, 5, 6, 5, 6, 7, 7, 8, 9 ] */

// function digits(num) {
//     let res = []
//     num = String(num)
//     for (let i = 0; i < num.length; i++)
//         for (let j = i + 1; j < num.length; j++)
//             res.push(Number(num[i]) + Number(num[j]))
//     return res
// }

function digits(num) {
    let res = [];
    [...String(num)].forEach((v, i, arr) => {
        for (let j = i + 1; j < arr.length; j++)
            res.push(Number(v) + Number(arr[j]))
    })
    return res
}

// const digits = num => [...num + ''].reduce((r, a, i, y) => r.concat(y.slice(i + 1).reduce((s, b) => s.concat(Number(a) + Number(b)), [])), [])
// const digits = num => [...num + ''].reduce((r, a, i) => r.concat([...num + ''].slice(i + 1).map(b => Number(a) + Number(b))), [])

q = digits(156) // [ 6, 7, 11 ]
q
q = digits(81596) // [ 9, 13, 17, 14, 6, 10, 7, 14, 11, 15 ]
q
q = digits(3852) // [ 11, 8, 5, 13, 10, 7 ]
q
q = digits(3264128) // [ 5, 9, 7, 4, 5, 11, 8, 6, 3, 4, 10, 10, 7, 8, 14, 5, 6, 12, 3, 9, 10 ]
q
q = digits(999999) // [ 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18 ]
q