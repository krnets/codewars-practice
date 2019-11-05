/* 7kyu - Sum of integers in string

Your task in this kata is to implement a function that 
calculates the sum of the integers inside a string. 
For example, in the string "The30quick20brown10f0x1203jumps914ov3r1349the102l4zy dog", 
the sum of the integers is 3635.
Only positive integers will be tested. */


const sumOfIntegersInString = s => (s.match(/\d+/g) || []).reduce((a, b) => a + Number(b), 0)
// const sumOfIntegersInString = s => (s.match(/\d+/g) || []).reduce((a, b) => a + b * 1, 0)


q = sumOfIntegersInString("12.4") // 16
q
q = sumOfIntegersInString("h3ll0w0rld") // 3
q
q = sumOfIntegersInString("2 + 3 = ") // 5
q
q = sumOfIntegersInString("Our company made approximately 1 million in gross revenue last quarter.") // 1
q
q = sumOfIntegersInString("The Great Depression lasted from 1929 to 1939.") // 3868
q
q = sumOfIntegersInString("Dogs are our best friends.") // 0
q
q = sumOfIntegersInString("C4t5 are 4m4z1ng.") // 18
q
q = sumOfIntegersInString("The30quick20brown10f0x1203jumps914ov3r1349the102l4zy dog") // 3635
q