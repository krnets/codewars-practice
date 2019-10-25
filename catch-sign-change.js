function catchSignChange(arr) {
    return arr.slice(1).reduce((prev, curr, index) => prev + (curr < 0 !== arr[0] < 0), 0)
}


// q = catchSignChange([1, 3, 4, 5]) // 0
// q
// q = catchSignChange([1, -3, -4, 0, 5]) // 2
// q
// q = catchSignChange([]) // 0
// q
q = catchSignChange([-47,84,-30,-11,-5,74,77]) // 3
q


// [1, -3, -4, 0, 5]
            //    ^
    // 0   1   0  1