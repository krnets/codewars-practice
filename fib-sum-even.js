// const fib = (n) => n <= 2 ? n : fib(n-1) + fib(n-2);
function* fib(n) {
    yield 2;

    let last = 1;
    let current = 2;

    while (true) {
        current = last + current;
        last = current - last;
        current = last + current;
        last = current - last;
        current = last + current;
        last = current - last;
        yield current;
    }
}

const fibSum = () => {
    let sum = 0;
    let gen = fib();
    let current = gen.next().value;
    while (current <= 4000000) {
        sum += current;
        current = gen.next().value;
    }
    return sum;
}


q = fibSum()
q