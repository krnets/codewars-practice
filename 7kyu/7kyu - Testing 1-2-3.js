// 7kyu - Testing 1-2-3

var number = function (array) {
    return array.map((v, i) => (i + 1) + ': ' + v)
}

q = number([]) // [], 'Empty array should return empty array'
q
q = number(["a", "b", "c"]) // ["1: a", "2: b", "3: c"], 'Return the correct line numbers'
q