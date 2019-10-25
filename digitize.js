function digitize(n) {
    // return String(n).split('').reverse().map(Number)
    return [...String(n)].map(Number).reverse()
}

q = digitize(35231) // [1,3,2,5,3])
q