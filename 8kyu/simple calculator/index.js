// 8kyu - simple calculator 

/* You are required to create a simple calculator that returns the result of addition, subtraction, 
multiplication or division of two numbers.

Your function will accept three arguments:
The first and second argument will be numbers.
The third argument will represent a sign indicating the operation to perform on these two numbers.

calculator(1,2,"+"); //=> result will be 3

if the variables are not numbers or the sign does not belong to the list above a message "unknown value" must be returned.

calculator(1,2,"&"); //=> result will be "unknown value"
calculator(1,"k","*"); //=> result will be "unknown value" */

// function calculator(a, b, sign) {
//     return ['+', '-', '*', '/'].includes(sign) && typeof a == 'number' && typeof b == 'number' ?
//         eval(a + sign + b) : 'unknown value'
// }

// const calculator = (a, b, sign) => '+-*/'.indexOf(sign) != -1 && typeof a == 'number' && typeof b == 'number' ? eval(a + sign + b) : 'unknown value'

// function calculator(a, b, sign) {
//     try { return eval(a + sign + b) } 
//     catch (e) { return 'unknown value' }
// }

// function calculator(a, b, sign) {
//     if (!isNaN(a) && !isNaN(b)) {
//         switch (sign) {
//             case '+': return a + b;
//             case '-': return a - b;
//             case '*': return a * b;
//             case '/': return a / b;
//         }
//     }
//     return 'unknown value'
// }

function calculator(a, b, sign) {
    if (isNaN(a) || isNaN(b) || /[^\+\-\*\/]/.test(sign)) return 'unknown value'
    return {
        '+': () => a + b,
        '-': () => a - b,
        '*': () => a * b,
        '/': () => a / b
    } [sign]()
}

q = calculator(1, 2, "+") // 3, "calculate"
q
q = calculator(1, 2, "-") // -1, "calculate"
q
q = calculator(3, 5, "*") // 15, "calculate"
q
q = calculator(6, 2, "/") // 3, "calculate"
q
q = calculator(6, 2, "$") // "unknown value", "calculate")
q
q = calculator(6, "h", "*") // "unknown value", "calculate"); 
q