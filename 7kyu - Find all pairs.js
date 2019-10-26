// 7kyu - Find all pairs

function duplicates(array) {
    let count = 0
    array.sort((a,b) => a - b)
    for (let i = 0; i < array.length; i++) {
        if (array[i] === array[i+1]) {
            count++
            i++
        }
    }
    return count
}

q = duplicates([1, 2, 5, 6, 5, 2]) // 2
q
q = duplicates([1, 2, 2, 20, 6, 20, 2, 6, 2]) // 4
q
q = duplicates([0, 0, 0, 0, 0, 0, 0]) // 3
q
q = duplicates([1000, 1000]) // 1
q
q = duplicates([]) // 0
q
q = duplicates([54]) // 0
q