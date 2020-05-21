const squareOfSums = (...args) => {
    const square = num => Math.pow(num, 2);
    return args
        .reduce((prev, curr) => prev + square(curr), 0)
}
// args.reduce((prev, curr) => prev + Math.pow(curr, 2), 0);  

q = squareOfSums(10, 5, 2, 3, 4, 7, 8, 1)
q