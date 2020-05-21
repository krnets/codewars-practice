// Beta - Die Rolling

/* Today your task is to build a basic die feature, where you will get a range in the form (min, max) - 
both included - and return a random number in the inclusive range.

Props if you don't use your language's random library! */

// const dice = (min, max) => Math.round(Math.random() * (max - min)) + min

// const dice = (min, max) => min + Math.round((Math.random()) * (max - min))

let _ = require('lodash')
const dice = (min, max) => _.sample(_.range(min, max))

q = dice(2, 7); // returns a value that can be 2, 3, 4, 5, 6, 7 */
q