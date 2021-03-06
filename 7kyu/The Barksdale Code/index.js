// 7kyu - The Barksdale Code

/* Fans of The Wire will appreciate this one. For those that haven't seen the show, 
the Barksdale Organization has a simple method for encoding telephone numbers exchanged via pagers: 
"Jump to the other side of the 5 on the keypad, and swap 5's and 0's."

Here's a keypad for visualization.

┌───┬───┬───┐
│ 1 │ 2 │ 3 │
├───┼───┼───┤
│ 4 │ 5 │ 6 │
├───┼───┼───┤
│ 7 │ 8 │ 9 │
└───┼───┼───┘
    │ 0 │
    └───┘

Detective, we're hot on their trail! We have a big pile of encoded messages here to use as evidence, 
but it would take way too long to decode by hand. Could you write a program to do this for us?

Write a funciton called decode(). Given an encoded string, return the actual phone number in string form. 
Don't worry about input validation, parenthesies, or hyphens. */

// const decode = (string) => string.replace(/\d/g, n => '5987604321'.indexOf(n))
const decode = (string) => string.replace(/./g, n => '5987604321'[n])

q = decode("4103432323") // "6957678787"
q
q = decode("4103438970") // "6957672135"
q
q = decode("4104305768") // "6956750342"
q
q = decode("4102204351") // "6958856709"
q
q = decode("4107056043") // "6953504567"
q
q = decode("4105753410") // "6950307695"
q