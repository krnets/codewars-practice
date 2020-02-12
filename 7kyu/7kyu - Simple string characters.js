// 7kyu - Simple string characters

/* In this Kata, you will be given a string and your task will be to return a list of ints 
detailing the count of uppercase letters, lowercase, numbers and special characters, as follows.

solve("*'&ABCDabcde12345") = [4,5,5,3]

--the order is: uppercase letters, lowercase, numbers and special characters. */

// function solve(s) {
//     let uppercase = s.match(/[A-Z]/g) || []
//     let lowercase = s.match(/[a-z]/g) || []
//     let numbers = s.match(/\d/g) || []
//     let specialChars = s.match(/[^a-z\d]/gi) || []
//     return [uppercase.length, lowercase.length, numbers.length, specialChars.length]
// }

const solve = s => [/[A-Z]/, /[a-z]/, /\d/, /\W/].map(rgx => s.split(rgx).length - 1)

q = solve('Codewars@codewars123.com') // [1,18,3,2]
q
q = solve('bgA5<1d-tOwUZTS8yQ') // [7,6,3,2]
q
q = solve('P*K4%>mQUDaG$h=cx2?.Czt7!Zn16p@5H') // [9,9,6,9]
q
q = solve("RYT'>s&gO-.CM9AKeH?,5317tWGpS<*x2ukXZD") // [15,8,6,9]
q
q = solve('$Cnl)Sr<7bBW-&qLHI!mY41ODe') // [10,7,3,6]
q
q = solve('@mw>0=QD-iAx!rp9TaG?o&M%l$34L.nbft') // [7,13,4,10]
q
