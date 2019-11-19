// 6kyu - Lowest product of 4 consecutive numbers

function lowestProduct(input) {
    if (input.length < 4)
        return 'Number is too small'
    for (var acc = [], i = 0; i < input.length - 3; i++)
        acc.push(input.slice(i, i + 4).split('')
            .reduce((a, b) => a * b, 1))
    return Math.min(...acc)
}


q = lowestProduct("123456789") // 24
q
q = lowestProduct("234567899") // 120
q
q = lowestProduct("2345611117899") // 1
q
q = lowestProduct("333") // 
q
q = lowestProduct("1234111") // 4
q