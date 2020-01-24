// 7kyu - heggeleggleggo

/* Egg Talk.

Insert an "egg" after each consonant. If there are no consonants, there will be no eggs. 
Argument will consist of a string with only alphabetic characters and possibly some spaces.


hello => heggeleggleggo
eggs => egegggegg

FUN KATA => FeggUNegg KeggATeggA

////

This Kata is designed for beginners to practice the basics of regular expressions. 
With this in mind a little bit of commenting in your solution could be very useful. */

// const heggeleggleggo = (str) => str.replace(/[^aeiou\s]/gi, match => match + 'egg')
const heggeleggleggo = (str) => str.replace(/([^aeiou\s])/gi, '$1egg')
// const heggeleggleggo = (str) => str.replace(/([^aeiou\s])/gi, '$&egg')

q = heggeleggleggo("hello") // "heggeleggleggo"
q
q = heggeleggleggo("code here") // "ceggodegge heggeregge"
q