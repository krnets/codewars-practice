// 7kyu - Algorithm Fun: Find The Unknown Number - Part II

function findUnknowNumber(a, b, c, x, y, z) {
    let n = 0
    while (++n)
        if ((n % a == x) && (n % b == y) && (n % c == z))
            return n
}

q = findUnknowNumber(3, 5, 7, 2, 3, 2) // 23
q
q = findUnknowNumber(3, 5, 7, 1, 2, 3) // 52
q
q = findUnknowNumber(3, 7, 11, 2, 1, 7) // 29
q
q = findUnknowNumber(2, 3, 5, 1, 1, 1) // 1
q