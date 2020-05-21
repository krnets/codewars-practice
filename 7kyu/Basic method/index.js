// 7kyu - Basic method

// Implement array method. Array will contain at least one item.

Array.prototype.max = function () {
    return Math.max(...this)
}

q = [2, 5, 1, 3].max() // returns 5
q
q = [1, 2, 3, 8, 4, 9, 7, 42, 99].max() // returns 99
q
q = [2, '5', 1, 3].max() // returns 5
q
q = [2, 5, 1, 'ab'].max() // returns NaN
q