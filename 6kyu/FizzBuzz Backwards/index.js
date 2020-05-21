// 6kyu - FizzBuzz Backwards

/* Traditionally in FizzBuzz, multiples of 3 are replaced by Fizz and multiples of 5 are replaced by Buzz. 
But we could also play FizzBuzz with any other integer pair [n,m] whose multiples are replaced with Fizz and Buzz.

For an array of numbers, Fizzes, Buzzes and FizzBuzzes, find the numbers whose multiples are being replaced by Fizz and Buzz. 
Return them as an array [n,m]

reverseFizzBuzz([1,2,"Fizz",4,"Buzz",6]) ==> [3,5]. 
Multiples of 3 are replaced by Fizz, multiples of 5 are replaced by Buzz

reverseFizzBuzz([1,"Fizz","Buzz","Fizz",5,"FizzBuzz"]) ==> [2,3]
Multiples of 2 are replaced by Fizz, multiples of 3 are replaced by Buzz

The Fizz and Buzz numbers will always be integers between 1 and 50, and the array will have a maximum length of 100. 
The Fizz and Buzz numbers might be equal, and might be equal to 1. */

// function reverseFizzBuzz(array) {
//     let fizz = array.map((v, i) => String(v).includes('Fizz') ? i + 1 : null).filter(Boolean)
//     let buzz = array.map((v, i) => String(v).includes('Buzz') ? i + 1 : null).filter(Boolean)
//     return [fizz[0], buzz[0]]
// }

const reverseFizzBuzz = array => [array.findIndex(v => /Fizz/.test(v)) + 1, array.findIndex(v => /Buzz/.test(v)) + 1]


q = reverseFizzBuzz([1, "FizzBuzz", 3, "FizzBuzz", 5, "FizzBuzz"]) // [2,2]
q
q = reverseFizzBuzz(["Fizz", "Fizz", "Fizz", "Fizz", "Fizz", "FizzBuzz"]) // [1,6]
q
q = reverseFizzBuzz([1, 2, "Fizz", 4, "Buzz"]) // [3,5]
q
q = reverseFizzBuzz([1, "Fizz", "Buzz", "Fizz", 5, "FizzBuzz"]) // [2,3]
q
q = reverseFizzBuzz([1, "FizzBuzz", 3, "FizzBuzz", 5, "FizzBuzz"]) // [2,2]
q
q = reverseFizzBuzz(["Fizz", "Fizz", "Fizz", "Fizz", "Fizz", "FizzBuzz"]) // [1,6]
q