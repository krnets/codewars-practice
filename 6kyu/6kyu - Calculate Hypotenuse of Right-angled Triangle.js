// 6kyu - Calculate Hypotenuse of Right-angled Triangle

/* To solve this Kata, complete the function, calculateHypotenuse(a,b), which will return the length of 
the hyptenuse for a right angled triangle with the other two sides having a length equal to the inputs. 

    The returned value should be a number rounded to three decimal places
    An error (ArgumentException in C#) should be thrown if an invalid input is provided 
    (inputs should both be numbers that are above zero)  */


function calculateHypotenuse(a, b) {
    if (a * 1 !== a || b * 1 !== b || a < 0 || b < 0)
        throw new Error('invalid input')
    return Math.hypot(a, b).toFixed(3)
}

q = calculateHypotenuse(1, 1) // returns 1.414
q
q = calculateHypotenuse(3, 4) // returns 5
q
q = calculateHypotenuse(-2, 1) // throws error
q
q = calculateHypotenuse("one", "two") // throws error
q