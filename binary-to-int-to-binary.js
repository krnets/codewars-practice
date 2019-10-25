function binaryToInt(n) {
    let parsed = parseInt(n, 2)
    return parsed
}
q = binaryToInt(11111)
q
//-----------------------------------//
function intToBinary(n) {
    let result = ''

    while (n > 0) {
        result = n % 2 + result
        n = Math.floor(n / 2)
    }
    return result
}
q = intToBinary(31)
q