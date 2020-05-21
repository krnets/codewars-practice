// Beta - Number of instances of n in a string

/* Write a function that finds the number of instances of n in a string.

For example if I ran the function instancesOfN('hello','l') it should return 2.
If I ran the function instancesOfN('hello mr coder man',' ') it should return 3.
If I ran the function instancesOfN('its so beautiful outside','z') it should return 'sorry no matches found'.

The first parameter of the argument should be the string that we are searching and the second parameter 
should be the number of times the second parameter occurs. 
If there are zero instances of the string the funciton should return 'sorry no matches found'. */

// function instancesOfN(string, letter) {
//     let res = string.split(letter).length - 1
//     return res == 0 ? 'sorry no matches found' : res
// }


const instancesOfN = (string, letter) => string.split(letter).length - 1 || 'sorry no matches found'


q = instancesOfN('hello there', 'l') // 2
q
q = instancesOfN('the cat in the hat', ' ') // 4
q
q = instancesOfN('this one more complex', 'z') // 'sorry no matches found'
q