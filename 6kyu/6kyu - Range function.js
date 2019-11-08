// 6kyu - Range function

function range(...rest) {
    let start = 1
    let step = 1
    let stop = 0

    if (rest.length == 1) {
        [stop] = rest
    }
    if (rest.length == 2) {
        [start, stop] = rest
    }
    if (rest.length == 3) {
        [start, step, stop] = rest
    }

    return Array.from({
        length: (stop - start) / step + 1
    }, (v, i) => start + (i * step))
}

q = range(5) // [1,2,3,4,5]
q
q = range(3, 7) // [3,4,5,6,7]
q
q = range(2, 3, 15) // [2,5,8,11,14]
q
q = range() // []
q