// 6kyu - Common array elements

// const common = (a, b, c) => a.filter(x => b.includes(x) && c.includes(x)).reduce((s, v) => s + v, 0)
function common(a, b, c) {
    let arrays = [a, b, c]
    arrays

    let inter = arrays.reduce((intersection, array) => {
        return intersection.filter(intersectedItem => array.some(item => intersectedItem === item));
    }, arrays[0])

    return inter.reduce((x, y) => x + y, 0)
}

q = common([1, 2, 3], [5, 3, 2], [7, 3, 2]) // 5
q
// q = common([1, 2, 2, 3], [5, 3, 2, 2], [7, 3, 2, 2]) // 7
// q