// 6kyu - Add commas to a number

/* Your task is to convert a given number into a string with commas added for easier readability. 
The number should be rounded to 3 decimal places and the commas should be added at intervals of 
three digits before the decimal point. There does not need to be a comma at the end of the number.

You will receive both positive and negative numbers.

commas(1) == "1"
commas(1000) == "1,000"
commas(100.2346) == "100.235"
commas(1000000000.23) == "1,000,000,000.23"
commas(-1) == "-1"
commas(-1000000.123) == "-1,000,000.123"  */


// const commas = num => num.toLocaleString()

// const commas = num => (+num.toFixed(3)).toString().replace(/\B(?=(\d{3})+(\.|$))/g, ',');

const commas = num => String(Number(num.toFixed(3))).replace(/\B(?=(\d{3})+(?!\d))/g, ',')


q = commas(1) // "1"
q
q = commas(1000) // "1,000"
q
q = commas(100.2346) // "100.235"
q
q = commas(1000000000.23) // "1,000,000,000.23"
q
q = commas(9123.212) // "9,123.212"
q
q = commas(-1) // "-1"
q
q = commas(-1000000.123) // "-1,000,000.123"
q