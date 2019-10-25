function basicOp(op, value1, value2) {
    switch (op) {
        case '+':
            return value1 + value2;
        case '-':
            return value1 - value2;
        case '*':
            return value1 * value2;
        case '/':
            return value1 / value2;
        default:
            return 0;
    }
}

q = basicOp('+', 4, 7) // 11
q
q = basicOp('-', 15, 18) // -3
q
q = basicOp('*', 5, 5) // 25
q
q = basicOp('/', 49, 7) //, 7
q