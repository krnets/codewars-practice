// 7kyu - Insert dashes

/* Write a function insertDash(num)/InsertDash(int num) that will insert dashes ('-') between each two odd numbers in num. 
For example: if num is 454793 the output should be 4547-9-3. Don't count zero as an odd number.

Note that the number will always be non-negative (>= 0). */

const insertDash = (num) => num.toString().replace(/[13579](?=[13579])/g, '$&-')


q = insertDash(454793) // '4547-9-3'
q
q = insertDash(123456) // '123456'
q
q = insertDash(1003567) // '1003-567'
q