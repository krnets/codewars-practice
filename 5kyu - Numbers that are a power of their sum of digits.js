// 5kyu - Numbers that are a power of their sum of digits

function powerSumDigTerm(n) {
    let array = []
    let start = 2
    let limit = 100
    let maxExponent = 42

    for (let a = start; a < limit; a++) {
        for (let b = start; b < maxExponent; b++) {
            let candidate = Math.pow(a, b)
            if ([...String(candidate)].reduce((x, y) => +y + x, 0) == a)
                array.push(candidate)
        }
    }
    return array.sort((a, b) => a - b)[n - 1]
}

// const s = [1, 81, 512, 2401, 4913, 5832, 17576, 0, 0, 390625, 614656, 1679616, 17210368, 34012224, 52521875, 60466176, 205962976, 612220032, 8303765625, 10460353203, 24794911296, 27512614111, 52523350144, 68719476736, 271818611107, 1174711139837, 2207984167552, 6722988818432, 20047612231936, 72301961339136, 248155780267521, 3904305912313344]

q = powerSumDigTerm(1) // 81
q
q = powerSumDigTerm(2) // 512
q
q = powerSumDigTerm(3) // 2401
q
q = powerSumDigTerm(4) // 4913
q