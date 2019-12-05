// 6kyu - IPv4 to int32

/* Take the following IPv4 address: 128.32.10.1 This address has 4 octets where each octet is a single byte (or 8 bits).

    1st octet 128 has the binary representation: 10000000
    2nd octet 32 has the binary representation: 00100000
    3rd octet 10 has the binary representation: 00001010
    4th octet 1 has the binary representation: 00000001

So 128.32.10.1 == 10000000.00100000.00001010.00000001

Because the above IP address has 32 bits, we can represent it as the 32 bit number: 2149583361.

Write a function ip_to_int32(ip) ( JS: ipToInt32(ip) ) that takes an IPv4 address and returns a 32 bit number.

  ipToInt32("128.32.10.1") => 2149583361

Fundamentals | Networks | Algorithms | Bits | Binary | Numbers | Integers | Utilities */

// const ipToInt32 = (ip) => parseInt(ip.split('.').map(v => Number(v).toString(2).padStart(8, 0)).join ``, 2)
// const ipToInt32 = (ip) => ip.split('.').reduce((int, v) => int * 256 + +v)
// const ipToInt32 = (ip) => ip.split('.').reduce((s, v) => 256 * s + Number(v), 0);
// const ipToInt32 = (ip) => ip.split('.').reduce((a, b) => a << 8 | b) >>> 0
// const ipToInt32 = (ip) => (ip = ip.split('.'), ((ip[0] << 24) + (ip[1] << 16) + (ip[2] << 8) + (ip[3] << 0)) >>> 0)
// function ipToInt32(ip) {
//     let array8 = new Uint8Array(ip.split('.').reverse().map(Number))
//     let array32 = new Uint32Array(array8.buffer);
//     return array32[0]
// }
const ipToInt32 = (ip) => ip.match(/\d+/g).reduce((n, x) => (n << 8) + parseInt(x), 0) >>> 0

q = ipToInt32("128.32.10.1") // 2149583361
q