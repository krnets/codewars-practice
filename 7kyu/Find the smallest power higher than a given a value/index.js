// 7kyu - Find the smallest power higher than a given a value

/* We have the number 12385. 
We want to know the value of the closest cube but higher than 12385. 
The answer will be 13824.

Now, another case. 
We have the number 1245678. 
We want to know the 5th power, closest and higher than that number. 
The value will be 1419857.

We need a function findNextPower in JavaScript that receives two arguments, a value val, and the exponent of the power, 
and outputs the value that we want to find.

findNextPower(12385, 3) == 13824
findNextPower(1245678, 5) == 1419857

The value, val will be always a positive integer.
The power, pow_, always higher than 1. */

// const findNextPower = (val, pow) => Math.ceil(Math.exp((1 / pow) * Math.log(val))) ** pow
const findNextPower = (val, pow) => Math.ceil(val ** (1 / pow)) ** pow

q = findNextPower(12385, 3) // 13824
q
q = findNextPower(1245678, 5) // 1419857
q
q = findNextPower(1245678, 6) // 1771561
q