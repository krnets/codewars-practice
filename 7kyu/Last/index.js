// 7kyu - Last

/* Find the last element of the given argument(s). */

// function last(...list) {
//     let a = String(list).split(',').slice(-1)
//     let b = Number(a)
//     return isNaN(b) ? a[0].slice(-1) : b
// }

// function last(list) {
//     let last = arguments[arguments.length - 1]
//     return last[last.length - 1] || last
// }

// function last(list) {
//     let args = [...arguments]
//     if (args.length > 1) return args[args.length - 1]
//     return list[list.length - 1] || list
// }

// function last(...list) {
//     return list[list.length - 1][list[list.length - 1].length - 1] || list[list.length - 1]
// }

// const last = (...list) => (
//     (list.length === 1) ? list = list[0] : null,
//     list[list.length - 1] || list
// )

// const last = (...list) => (list.length > 1 ? list : list = list[0],
//     list[list.length - 1] || list)

const last = (...list) => (list.length > 1 ? list : list = list[0], list[list.length-1] || list)

// function last(list) {
//     let a = list.length > 1 ? list : [].slice.call(arguments)
//     return a[a.length - 1]
// }

q = last([1, 2, 3, 4, 5]) // 5   -- array
q
q = last("abcde") // "e"         -- string
q
q = last(1, "b", 3, "d", 5) // 5 -- arguments
q
q = last([1, 2, 3, 4, 10]) // 5  -- array
q