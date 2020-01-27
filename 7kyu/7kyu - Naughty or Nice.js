// 7kyu - Naughty or Nice?

/* Unfortunately, Santa's Javascript and CoffeeScript Elves accidentally mixed the Naughty and Nice list together! 
Santa needs your help to save Christmas!

Santa needs you to write two functions, getNiceNames and getNaughtyNames. Both of the functions accept an array of objects. 
getNiceNames returns an array containing only the names of the nice people, and getNaughtyNames returns an array containing 
only the names of the naughty people. Return an empty array [] if the result from either of the functions contains no names.

The objects in the passed in array will represent people. Each object contains two properties: name and wasNice.

name - The name of the person
wasNice - True if the person was nice this year, false if they were naughty

Person Object Examples
JavaScript

  { name: 'Warrior reading this kata', wasNice: true }
  { name: 'xDranik', wasNice: false } */

var naughty = [{ name: 'xDranik', wasNice: false }]
var nice = [{ name: 'Santa', wasNice: true }, { name: 'Warrior reading this kata', wasNice: true } ];

const getNiceNames = (people) => people.filter(v => v.wasNice).map(v => v.name)

const getNaughtyNames = (people) => people.filter(v => !v.wasNice).map(v => v.name)

q = getNiceNames(naughty) // []
q
q = getNaughtyNames(nice) // []
q
q = getNiceNames(nice.concat(naughty)) //  
q
q = getNaughtyNames(nice.concat(naughty)) // [ xDranik ]
q