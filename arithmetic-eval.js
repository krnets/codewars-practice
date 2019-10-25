function arithmetic(a, b, operator) {
    let dict = {
        add: '+',
        subtract: '-',
        multiply: '*',
        divide: '/'
    }
    return eval(a + dict[operator] + b)
}

// const arithmetic = (a, b, operator) => ({
//     add: a + b,
//     subtract: a - b,
//     multiply: a * b,
//     divide: a / b
// } [operator])

// const arithmetic = (a, b, operator) => eval(a + {add:'+',subtract:'-',multiply:'*',divide:'/'}[operator] + b)

q = arithmetic(1, 2, "add") // 3, "'add' should return the two numbers added together!"
q
q = arithmetic(8, 2, "subtract") // 6, "'subtract' should return a minus b!"
q
q = arithmetic(5, 2, "multiply") // 10, "'multiply' should return a multiplied by b!"
q
q = arithmetic(8, 2, "divide") // 4, "'divide' should return a divided by b!"
q