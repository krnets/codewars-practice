function product(values) {
    return values === null || values.length == 0 ? null :
           values.reduce((a, b) => a * b, 1)
}
// function product(values) {
//     return values && values.length ? 
//            values.reduce((a, b) => a * b, 1) : 
//            null
// }
// const product = (values) => values && values.length ? values.reduce((a, b) => a * b, 1) : null

q = product([5, 4, 1, 3, 9]) // 540
q
q = product([-2, 6, 7, 8]) // -672
q
q = product([10]) // 10
q
q = product([0, 2, 9, 7]) // 0
q
q = product(null) // null
q
q = product([]) // null
q