// 7kyu - Fizz Buzz - Without ifs

/* Implement a function that applies the standard fizz buzz test:

    If a number is divisible by 3, return Fizz
    If it is divisible by 5, return Buzz
    If it is divisible by both 3 and 5, return FizzBuzz
    If it is not divisible by 3 or 5, return the number itself

However, when making the function, you cannot use if (meaning else is also not an option).

    A number will always be provided
    The number provided will always be positive and an integer */

// const fizzBuzz = (n) => n % 3 == 0 && n % 5 == 0 ? 'FizzBuzz' : n % 3 == 0 ? 'Fizz' : n % 5 == 0 ? 'Buzz' : n
const fizzBuzz = (n) => n % 15 ? n % 5 ? n % 3 ? n : 'Fizz' : 'Buzz' : 'FizzBuzz'

q = fizzBuzz(1) // 1
q
q = fizzBuzz(3) // "Fizz"
q
q = fizzBuzz(6) // "Fizz"
q
q = fizzBuzz(7) // 7
q
q = fizzBuzz(10) // "Buzz"
q
q = fizzBuzz(30) // "FizzBuzz"
q