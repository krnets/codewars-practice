// Beta - Multiplication sequence - part 1

function multiplication(n) {
    [a, b] = [1, 2]
    while (n--)
        [a, b] = [b, a * b]
    return a
}

q = multiplication(0) // 1
q
q = multiplication(1) // 2
q
q = multiplication(2) // 2
q
q = multiplication(3) // 4
q
q = multiplication(6) // 256
q