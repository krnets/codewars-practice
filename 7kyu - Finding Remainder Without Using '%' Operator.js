// 7kyu - Finding Remainder Without Using '%' Operator

const remainder = (Divident, divisor) => {
    if (divisor == 0) return 'NaN'

    while (Divident > 0) {
        let temp = Divident - divisor
        if (temp < 0) 
            return Divident
        Divident = temp
    }
    return Divident
}

// const remainder = (D, d) => d == 0 ? 'NaN' : D - (d * ~~(D / d))
// const remainder = (D, d) => d == 0 ? 'NaN' : D - (Math.trunc(D / d) * d)
// const remainder = (D, d) => d ? D - (Math.trunc(D / d) * d) : 'NaN'
// const remainder = (a, b) => b ? eval(a + String.fromCharCode(37) + b) : 'NaN'
// const remainder = (D, d) => d ? D - (D / d | 0) * d : 'NaN'

q = remainder(3, 2) // 1
q
q = remainder(19, 2) // 1
q
q = remainder(10, 2) // 0
q
q = remainder(34, 7) // 6
q
q = remainder(27, 5) // 2
q
q = remainder(27, 0) // NaN
q