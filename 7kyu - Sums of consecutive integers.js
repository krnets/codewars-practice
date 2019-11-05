/** 7kyu - Sums of consecutive integers
 * 
 * Given the number of consecutive integers and the total of the integers,
 * return the consecutive integer at the requested position.
 *
 * @param {int} x number of consecutive integers
 * @param {int} y sum of consecutive integers
 * @param {int} n position of requested integer
 * @return {int} consecutive integer at requested position
 */

const position = (x, y, n) => Math.ceil(y / x) - Math.floor(x / 2) + n

// const position = (x, y, n) => y / x - (x - 1) / 2 + n

q = position(4, 14, 3) // 5
q
q = position(2, 25, 0) // 12
q
q = position(7, 749, 5) //109
q

q = position(3, -9, 1) // -3
q
q = position(5, 0, 0) // -2
q