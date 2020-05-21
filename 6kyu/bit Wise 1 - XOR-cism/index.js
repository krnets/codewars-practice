// 6kyu - bit "Wise" #1: XOR-cism

/* Series: bit “Wise”

Javascript’s bitwise operators are probably the least used and least widely understood part of the language: 
In the domain of the web, where Javascript enjoys unrivaled supremacy, operating on the bits-and-bytes level is 
often abstracted away (perhaps thankfully). Despite this, there remain practical uses for the language’s 
bitwise operators both on the web (for performance reasons) and especially in the burgeoning field of physical computing 
(Arduino, RaspberryPi, etc.), where Javascript is being embedded in and interacting with things like sensor packages, 
shift registers and other electronic components that “speak binary”. In this series of Kata, we’ll familiarize ourselves 
with some of the “basic moves” of the JS bitwise operators.

Exercise 1: XOR-cism
In this Kata, you will be writing a function named "swapper" that should "swap" two integer values (a and b) and 
return them in an array in "swapped" order. Do your best to complete the kata without declaring any variables or 
functions and using only bitwise operators in the body of the 'swapper' function. There are some pre-loaded hints 
you can access if you need help doing it with the bitwise operators. Good luck. */

/*
 HINTS: uncomment out the following line
 for a series of hints to help you with the 
 bitwise stuff if you get stuck...
 (There are three HINTS indexed 0,1, and 2, respectively)
*/
//console.log(HINTS[0]);

// function swapper(a, b) {
//     a = a ^ b
//     b = a ^ b
//     a = a ^ b
//     return [a, b]
// }

function swapper(a, b) {
    a ^= b
    b ^= a
    a ^= b
    return [a, b]
}

// const swapper = (a, b) => [(a ^ a) ^ b, (b ^ b) ^ a]

q = swapper(0, 1); //returns [1, 0]
q
q = swapper(1, 2) // [2,1]
q