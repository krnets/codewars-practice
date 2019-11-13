// 6kyu - Find The Parity Outlier

function findOutlier(integers) {
    let odds = integers.filter(v => v % 2 != 0)
    let evens = integers.filter(v => v % 2 == 0)

    return odds.length < evens.length ? odds[0] : evens[0]
}

q = findOutlier([0, 1, 2]) // 1
q
q = findOutlier([1, 2, 3]) // 2
q
q = findOutlier([2, 6, 8, 10, 3]) // 3
q
q = findOutlier([0, 0, 3, 0, 0]) // 3
q
q = findOutlier([1, 1, 0, 1, 1]) // 0
q