// 5kyu - Make the sum... if you can.

/* This kata is about sum two positive numbers. You are given an incomplete function that receives number1 and number2, then must return the sum of these two numbers, that could be decimal with precision of two digits. Write your add function, plus, the following operators are disabled: +, -.

add(210, 210) => 420 //should return the sum
add(1.5, 1.6) => 3.1   //must work with decimals
add(1.001, 1) => 2   //precision of two decimal digits

    Notes:
    1 - Sum of two positive numbers.
    2 - Round both numbers to a precision of 2 digits first.
    3 - Parameters can be ```undefined``` and ```undefined``` should be considered as ```0```. */

function add(a, b) {
    a = Math.round(a * 100 || 0)
    b = Math.round(b * 100 || 0)
    return Array(a).concat(Array(b)).length / 100
}


q = add("21", "21") // 42
q
q = add(1994, 1994) // 3988
q
q = add(true, false) // 1
q
q = add(4, undefined) // 4
q
q = add(0, 0) // 0
q
q = add(210, 210) // 420 //should return the sum
q
q = add(1.5, 1.6) // 3.1   //must work with decimals
q
q = add(1.001, 1) // 2   //precision of two decimal digits
q