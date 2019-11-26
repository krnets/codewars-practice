// 6kyu - IP Address to Number

/* Create the function ipToNum that takes an ip address and converts it to a number, 
as well as the function numToIp that takes a number and converts it to an IP address string. 
Input will always be valid.

##Conversion Example

//original IP address
192.168.1.1

//breaks down into 4 binary octets
11000000 . 10101000 . 00000001 . 00000001

//which are merged together (unsigned 32-bit binary)
11000000101010000000000100000001

//and finally converted to base 10
3232235777

Note that the binary octets are not using two's complement (so we can't have negative numbers) 
even though JavaScript numbers do.

##Code Examples

###ipToNum

ipToNum('192.168.1.1') //returns 3232235777
ipToNum('10.0.0.0') //returns 167772160
ipToNum('176.16.0.1') //returns 2953838593

###numToIp

numToIp(3232235777) //returns '192.168.1.1'
numToIp(167772160) //returns '10.0.0.0'
numToIp(2953838593) //returns '176.16.0.1'

###nested

numToIp(ipToNum('192.168.1.1')) //returns '192.168.1.1'
ipToNum(numToIp(3232235777)) //returns 3232235777

Fundamentals | Strings | Numbers | Formatting | Algorithms | Binary | Networks | Encoding | Decoding | Utilities */


function ipToNum(ip) {
    return parseInt(ip.split('.').map(v => Number(v).toString(2).padStart(8, 0)).join(``), 2)
}

function numToIp(num) {
    let binaryString = ''
    while (num > 0) {
        binaryString = num % 2 + binaryString
        num = Math.floor(num / 2)
    }
    let paddedBinary = binaryString.padStart(32, 0)
    let octets = []
    for (let i = 0; i < 32; i += 8)
        octets.push(paddedBinary.slice(i, i + 8))
    return octets.map(v => parseInt(v, 2)).join('.')
}

// const ipToNum = ip => ip.split('.').reduce((sum, x) => sum << 8 | x, 0) >>> 0
// const numToIp = num => [num >>> 24, num >> 16 & 255, num >> 8 & 255, num & 255].join('.')

// const ipToNum = ip => ip.split(".").reduce((a, b) => a * 256 + +b)
// const numToIp = num => ("00000000" + num.toString(2)).substr(-32).match(/.{8}/g).map(x => parseInt(x, 2)).join('.')

// const ipToNum = ip => ip.split `.`.reduce((r, e) => r * 256 + +e)
// const numToIp = num => ('0'.repeat(32 - (num = num.toString(2)).length) + num)
//     .replace(/(\d{8})(?!$)/g, '$1.').split `.`
//     .map(e => parseInt(e, 2)).join `.`

// const ipToNum = ip => parseInt(ip.split('.').map(x => (+x).toString(2)).map(x => '0'.repeat(8 - x.length) + x).join(''), 2)
// const numToIp = num => num.toString(2).match(/^(.*)(.{8})(.{8})(.{8})$/).slice(1).map(x => parseInt(x, 2)).join('.')



//ipToNum
q = ipToNum('192.168.1.1') // 3232235777
q
q = ipToNum('10.0.0.0') // 167772160
q
q = ipToNum('176.16.0.1') // 2953838593
q

//numToIp
q = numToIp(3232235777) // '192.168.1.1'
q
q = numToIp(167772160) // '10.0.0.0'
q
q = numToIp(2953838593) // '176.16.0.1'
q

//Combined
q = numToIp(ipToNum('192.168.1.1')) // '192.168.1.1'
q
q = numToIp(ipToNum('10.0.0.0')) // '10.0.0.0'
q
q = numToIp(ipToNum('176.16.0.1')) // '176.16.0.1'
q
q = ipToNum(numToIp(3232235777)) // 3232235777
q
q = ipToNum(numToIp(167772160)) // 167772160
q
q = ipToNum(numToIp(2953838593)) // 2953838593
q