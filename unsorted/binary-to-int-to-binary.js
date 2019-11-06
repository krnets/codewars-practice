function binaryToInt(n) {
    let intFromBinary = parseInt(n, 2)
    return intFromBinary
}
q = binaryToInt(11111)
q
//-----------------------------------//
function intToBinary(n) {
    let binaryString = ''
    while (n > 0) {
        binaryString = n % 2 + binaryString
        n = Math.floor(n / 2)
    }
    return binaryString
}
q = intToBinary(31)
q