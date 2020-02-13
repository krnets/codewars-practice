// 7kyu - Find the calculation type

/* You have to create a function which receives 3 arguments: 2 numbers, and the result of an unknown operation 
performed on them (also a number).

Based on those 3 values you have to return a string, that describes which operation was used to get the given result.

The possible return strings are: "addition", "subtraction", "multiplication", "division".

calcType(1, 2, 3) -->   1 ? 2 = 3   --> "addition"

    In case of division you should expect that the result of the operation is obtained by using / operator 
    on the input values - no manual data type conversion or rounding should be performed.
    Cases with just one possible answers are generated.
    Only valid arguments will be passed to the function. */

// const calcType = (a, b, res) => a + b == res ? 'addition' : a / b == res ? 'division' : a * b == res ? 'multiplication' : 'subtraction'

function calcType(a, b, res) {
    return {
        [a + b]: 'addition',
        [a - b]: 'subtraction',
        [a * b]: 'multiplication',
        [a / b]: 'division'
    }[res]
}

q = calcType(1, 2, 3) // 'addition'
q
q = calcType(10, 4, 40) // 'multiplication'
q
q = calcType(10, 5, 5) // 'subtraction'
q
q = calcType(9, 5, 1.8) // 'division'
q
