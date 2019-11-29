// 7kyu - Geometric Progression Sequence

// Write a function that will print first n elements of the sequence with the given constant r and first element a.
// Result should be separated by comma and space.

function geometricSequenceElements(a, r, n) {
    let res = [a]
    for (let i = 0; i < n - 1; i++)
        res.push(res[i] * r)
    return res.join(', ')
}

// const geometricSequenceElements = (a, r, n) => n === 1 ? '' + a :
//     `${geometricSequenceElements(a, r, n - 1)}, ${a * Math.pow(r, n - 1)}`

// const geometricSequenceElements = (a, r, n) => [...Array(n)].map((_, i) => a * Math.pow(r, i)).join(', ')
// const geometricSequenceElements = (a, r, n) => [...Array(n)].map((_, i) => a * r ** i).join(', ')



q = geometricSequenceElements(2, 3, 5), '2, 6, 18, 54, 162'
q
q = geometricSequenceElements(2, 2, 10), '2, 4, 8, 16, 32, 64, 128, 256, 512, 1024'
q
q = geometricSequenceElements(1, -2, 10), '1, -2, 4, -8, 16, -32, 64, -128, 256, -512'
q