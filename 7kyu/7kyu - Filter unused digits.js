// 7kyu - Filter unused digits

/* Given few numbers, you need to print out the digits that are not being used.
    Result string should be sorted
    The test case won't pass Integer with leading zero */


function unusedDigits(...vals) {
    vals = [...vals.join('')]
    return [...Array(10).keys()].filter(v => !vals.includes(String(v))).join('')
}

// const unusedDigits = (...d) => [...'0123456789'].filter(v => !d.join ``.includes(v)).join ``
// const unusedDigits = (...d) => [...Array(10).keys()].filter(v => !d.join ``.includes(v)).join ``

q = unusedDigits(12, 34, 56, 78) // "09"
q
q = unusedDigits(2015, 8, 26) // "3479"
q