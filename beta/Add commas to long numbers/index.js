// Beta - Add commas to long numbers

/* In representing large numbers, from the right side to the left, English texts usually use commas to separate 
each group of three digits in front of the decimal.

Input: A number. (only positive integers in this kata)
Output: The number formatted with commas.

1          -> "1"
256        -> "256"
65536      -> "65,536"
4294967296 -> "4,294,967,296" */


// const comma = num => num.toLocaleString()

// const comma = num => String(num).replace(/\B(?=(\d{3})+(?!\d))/g, ',')

const comma = num => String(num).replace(/\B(?=(\d{3})+$)/g, ',')


q = comma(1) // "1"
q
q = comma(256) // "256"
q
q = comma(65536) // "65,536"
q
q = comma(4294967296) // "4,294,967,296"
q