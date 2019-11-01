function flattenAndSort (array) {
    // return arr.flat().sort((a,b) => a - b)
    return array
        .reduce((a,b) => a.concat(b),[])
        .sort((a,b) => a - b)
}

q = flattenAndSort([]) //, []
q
q = flattenAndSort([[], [1]]) //, [1]
q
q = flattenAndSort([[3, 2, 1], [7, 9, 8], [6, 4, 5]]) //, [1, 2, 3, 4, 5, 6, 7, 8, 9]
q
q = flattenAndSort([[1, 3, 5], [100], [2, 4, 6]]) //, [1, 2, 3, 4, 5, 6, 100]
q