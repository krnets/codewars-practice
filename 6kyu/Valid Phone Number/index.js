// 6kyu - Valid Phone Number

/* Write a function that accepts a string, and returns true if it is in the form of a phone number.
Assume that any integer from 0-9 in any of the spots will produce a valid phone number.

Only worry about the following format:
(123) 456-7890 (don't forget the space after the close parentheses)

Algorithms | Regular Expressions | Declarative Programming | Advanced Language Features | Fundamentals | Strings */

// const validPhoneNumber = phoneNumber => /^\(\d{3}\)\s\d{3}\-\d{4}$/.test(phoneNumber)
const validPhoneNumber = phoneNumber => /^\(\d{3}\) \d{3}\-\d{4}$/.test(phoneNumber)
// const validPhoneNumber = RegExp.prototype.test.bind(/^\(\d{3}\) \d{3}-\d{4}$/)

q = validPhoneNumber("(123) 456-7890") // true
q
q = validPhoneNumber("(1111)555 2345") // false
q
q = validPhoneNumber("(098) 123 4567") // false
q