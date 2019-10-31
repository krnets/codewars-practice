// 7kyu - Simple Fun 144 - Distinct Digit Year

const distinctDigitYear = year => /(.).*\1/.test(`${year+1}`) ? distinctDigitYear(year + 1) : year + 1


q = distinctDigitYear(1987) // 2013
q
q = distinctDigitYear(2013) // 2014
q