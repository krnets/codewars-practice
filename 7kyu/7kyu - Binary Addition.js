function addBinary(a, b) {
    let result = ''
    let sum = a + b

    while (sum > 0) {
        result = sum % 2 + result
        sum = Math.floor(sum / 2)
    }
    return result
}

const addBinary = (a, b) => (a + b).toString(2);

function addBinary(a, b) {
    return ((a + b) >>> 0).toString(2);
}

function addBinary(a, b) {
    return (a + b).toString(2)
}

function addBinary(a, b) {
    return Number(a + b).toString(2);
}

function decimalToBinary(decimal) {
    return (decimal >>> 0).toString(2);
}

function addBinary(a, b) {
    return decimalToBinary(a + b);
}