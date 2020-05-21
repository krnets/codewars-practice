// 6kyu - IP Validation

/* Write an algorithm that will identify valid IPv4 addresses in dot-decimal format. 
IPs should be considered valid if they consist of four octets, with values between 0 and 255, inclusive.
Input to the function is guaranteed to be a single string.

Valid inputs:
1.2.3.4
123.45.67.89

Invalid inputs:
1.2.3
1.2.3.4.5
123.456.78.90
123.045.067.089

Note that leading zeros (e.g. 01.02.03.04) are considered invalid.
Algorithms | Regular Expressions | Declarative Programming | Advanced Language Features | Fundamentals | Strings */

function isValidIP(str) {
    if (!str.match(/^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$/) || str.match(/^\s|^0\d|(\.0\d)|\s$/)) return false
    return str.split('.').filter(v => v > 255).length < 1
}

// const isValidIP = str => (p = str.split('.'), p.length == 4 && p.every(n => /^\d+$/.test(n) && n == String(Number(n)) && n > -1 && n < 256))
// const isValidIP = str => str.split('.').filter(n => /^\d+$/.test(n) && n == String(Number(n)) && n > -1 && n < 256).length == 4
// const isValidIP = str => str.split('.').filter(v => v == Number(v).toString() && Number(v) < 256).length == 4;
// const isValidIP = str => /^(([1-9]?\d|1\d\d|2[0-4]\d|25[0-5])(\.(?!$)|$)){4}$/.test(str)

// const net = require('net')
// const isValidIP = str => net.isIP(str) == 4

// import { isIP } from 'net'
// const isValidIP = str => isIP(str) == 4


q = isValidIP("0.0.0.0") // true
q
q = isValidIP("12.255.56.1") // true
q
q = isValidIP("137.255.156.100") // true
q
q = isValidIP("00.101.233.11") // false
q
q = isValidIP('') // false
q
q = isValidIP('abc.def.ghi.jkl') // false
q
q = isValidIP('123.456.789.0') // false
q
q = isValidIP('12.34.56') // false
q
q = isValidIP('01.02.03.04') // false
q
q = isValidIP('256.1.2.3') // false
q
q = isValidIP('1.2.3.4.5') // false
q
q = isValidIP('123,45,67,89') // false
q
q = isValidIP('1e0.1e1.1e2.2e2') // false
q
q = isValidIP(' 1.2.3.4') // false
q
q = isValidIP('1.2.3.4 ') // false
q
q = isValidIP('12.34.56.-7') // false
q
q = isValidIP('1.2.3.4\n') // false
q
q = isValidIP('\n1.2.3.4') // false
q