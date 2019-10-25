function add(x) {
    return function (y) {
        return x + y;
    }
}

function subtract(x) {
    return function (y) {
        return x - y;
    }
}

function multiply(x) {
    return function (y) {
        return x * y;
    }
}

function divide(x) {
    return function (y) {
        return x / y;
    }
}

function apply(fn) {
    return function (x, y) {
        return fn(x, y);
    }
}

q = add(3)(4) // 7
q
q = subtract(3)(4) // -1
q
q = multiply(3)(4) // 12
q
q = apply(add)(3)(4) // 7
q
q = apply(subtract)(3)(4) // -1
q
q = apply(multiply)(3)(4) //12
q