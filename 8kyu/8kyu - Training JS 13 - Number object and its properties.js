// 8kyu - Training JS 13 - Number object and its properties

function whatNumberIsIt(n) {
    return `Input number is ${n ==  'Infinity' ? 'Number.POSITIVE_INFINITY' : 
                              n == '-Infinity' ? 'Number.NEGATIVE_INFINITY' :
                              n == 1.7976931348623157e308 ? 'Number.MAX_VALUE' :
                              n == 5e-324 ? 'Number.MIN_VALUE' :
                              isNaN(n) ? 'Number.NaN' :
                              n}`
}

q = whatNumberIsIt(1/0) // "Input number is Number.POSITIVE_INFINITY
q
q = whatNumberIsIt(100) // "Input number is 100
q
q = whatNumberIsIt(1.7976931348623157e+308) // "Input number is Number.MAX_VALUE
q
q = whatNumberIsIt(5e-324) // "Input number is Number.MIN_VALUE
q
q = whatNumberIsIt(-Number.MAX_VALUE*2) // "Input number is Number.NEGATIVE_INFINITY
q
q = whatNumberIsIt(NaN) // "Input number is Number.NaN
q
q = whatNumberIsIt(Infinity+1) // "Input number is Number.POSITIVE_INFINITY
q
