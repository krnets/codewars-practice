// 7kyu - Sum The Array

Array.prototype.sum = function () {
    return this.reduce((a, b) => a + b, 0)
}

var tests = [[[1, 2, 3, 4], 10],
    [[2, 4, 6, 8], 20],
    [[93, 31, 62, 103], 289],
    [[397, 403, 764, 142], 1706]]

tests.forEach(function (x) {
    return (x[0].sum(), x[1]);
})

tests