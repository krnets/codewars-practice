// 7kyu - 254 shades of grey

/* Why would we want to stop to only 50 shades of grey? Let's see to how many we can go.

Write a function that takes a number n as a parameter and return an array containing n shades of grey in hexadecimal code 
(#aaaaaa for example). The array should be sorted in ascending order starting with #010101, #020202, etc. (using lower case letters).


As a reminder, the grey color is composed by the same number of red, green and blue: #010101, #aeaeae, #555555, etc. 
Also, #000000 and #ffffff are not accepted values.

When n is negative, just return an empty array. If n is higher than 254, just return an array of 254 elements. */

// function shadesOfGrey(n) {
//     let shades = []
//     for (let i = 0; i < Math.min(n, 254); i++)
//         shades.push('#' + ('0' + i.toString(16)).slice(-2).repeat(3))
//     return shades
// }

const shadesOfGrey = (n) => n > 0 ? Array(Math.min(n, 254)).fill().map((_, i) => '#' + ('0' + (i + 1).toString(16)).slice(-2).repeat(3)) : []
// const shadesOfGrey = (n) => n > 0 ? Array(Math.min(n, 254)).fill().map((_, i) => '#' + ((i + 1).toString(16)).padStart(2, '0').repeat(3)) : []
// const shadesOfGrey = (n) => n > 0 ? Array(Math.min(n, 254)).fill().map((_, i) => '#' + ((++i < 16 ? '0' : '') + i.toString(16)).repeat(3)) : []

q = shadesOfGrey(255)
q