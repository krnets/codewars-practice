// 7kyu - Substituting Variables Into Strings: Padded Numbers

// Complete the solution so that it returns a formatted string. 
// The return value should equal "Value is VALUE" where value is a 5 digit padded number.

// const solution = value => `Value is ${String(value).padStart(5,'0')}`
const solution = value => 'Value is ' + String(value).padStart(5, '0')

q = solution(5) // "Value is 00005"
q