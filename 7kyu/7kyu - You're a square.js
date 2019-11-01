function isSquare(n) {
    // return  Math.sqrt(n) == Math.floor(Math.sqrt(n))
    // return [Math.sqrt(n), Math.floor(Math.sqrt(n))]
    // return Math.sqrt(n) % 1 == 0
    // return Number.isInteger(Math.sqrt(n))
    return /^[0-9]+$/.test(Math.sqrt(n))
}

q = isSquare(-1) // false, "-1: Negative numbers cannot be square numbers");
q
q = isSquare( 0) // true, "0 is a square number (0 * 0)");
q
q = isSquare( 3) // false, "3 is not a square number");
q
q = isSquare( 4) // true, "4 is a square number (2 * 2)");
q
q = isSquare(25) // true, "25 is a square number (5 * 5)");
q
q = isSquare(26) // false, "26 is not a square number");
q