function binaryCleaner(arr) {
    let cleanArray = arr.filter(v => v < 2)
    let indexesRemoved = []
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] > 1)
            indexesRemoved.push(i)
    }
    return [cleanArray, indexesRemoved]
}

q = binaryCleaner([0, 1, 2, 1, 0, 2, 1, 1, 1, 0, 4, 5, 6, 2, 1, 1, 0])
// [ [ 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0 ], [ 2, 5, 10, 11, 12, 13 ] ], "Should return"
q
q = binaryCleaner([0, 1, 1, 2, 0])
// [ [ 0, 1, 1, 0 ], [ 3 ] ], "Should return"
q
q = binaryCleaner([2, 2, 0])
// [ [ 0 ], [ 0, 1 ] ], "Should return: "
q
q = binaryCleaner([0, 1, 2, 1, 0, 2, 1, 1])
// [ [ 0, 1, 1, 0, 1, 1 ], [ 2, 5 ] ], "Should return"
q
q = binaryCleaner([1])
// [ [ 1 ], [] ], "Should return"
q