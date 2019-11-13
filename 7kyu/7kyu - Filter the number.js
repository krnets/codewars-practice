// 7kyu - Filter the number

// var FilterString = function (value) {
//     return +[...value].filter(v => Number(v) == v).join ``
// }

var FilterString = function (value) {
    return +value.replace(/\D/g, '')
}

q = FilterString("123") // 123
q
q = FilterString("a1b2c3") // 123
q
q = FilterString("aa1bb2cc3dd") // 123
q