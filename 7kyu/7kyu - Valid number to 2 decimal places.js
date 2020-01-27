// 7kyu - Valid number to 2 decimal places

/* Check that a number is a valid number that has been given to 2 decimal places. 
The number passed to the function will be given as a string. If the number satisfies the criteria below, 
the function should return true, else it should return false. Please check the criteria for a valid number:

optional + or - symbol in front
optional digits before a decimal point
a decimal point
exactly two digits after the point
nothing else

Examples of valid and non-valid numbers

Valid numbers: [ "0.00" "3.90" "1000.00" ".00" "-2.55" "+2.10" "-.55"]
Non-valid numbers: ["hellow 11.99" "11.9" "11" "11." ".9"] */

const validNumber = (num) => /^[+-]?\d*\.\d\d$/.test(num)


q = validNumber("0.00") // true
q
q = validNumber(".00") // true
q
q = validNumber("-.00") // true
q
q = validNumber(".30") // true
q
q = validNumber("0.40") // true
q
q = validNumber("34443.33") // true
q
q = validNumber(".0a") // false
q
q = validNumber("1.00.") // false
q
q = validNumber(".+00") // false
q
q = validNumber("w.00") // false
q
q = validNumber("..00") // false
q
q = validNumber("1,00") // false
q