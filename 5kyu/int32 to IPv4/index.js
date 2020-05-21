// 5kyu - int32 to IPv4

/* Take the following IPv4 address: 128.32.10.1
This address has 4 octets where each octet is a single byte (or 8 bits).

    1st octet 128 has the binary representation: 10000000
    2nd octet 32 has the binary representation: 00100000
    3rd octet 10 has the binary representation: 00001010
    4th octet 1 has the binary representation: 00000001

So 128.32.10.1 == 10000000.00100000.00001010.00000001
Because the above IP address has 32 bits, we can represent it as the unsigned 32 bit number: 2149583361

Complete the function that takes an unsigned 32 bit number and returns a string representation of its IPv4 address.
2149583361 ==> "128.32.10.1"
32         ==> "0.0.0.32"
0          ==> "0.0.0.0"

Algorithms | Networks | Bits | Binary | Utilities */

// const int32ToIp = (int32) => (int32 == 0) ? '0.0.0.0' : int32.toString(2).match(/.{8}/g).map(v => parseInt(v, 2)).join('.')
// const int32ToIp = (int32) => int32.toString(2).padStart(32, '0').match(/([01]{8})/g).map(x => parseInt(x, 2)).join('.')
// const int32ToIp = (int32) => (int32 >>> 24) + "." + (int32 >> 16 & 255) + "." + (int32 >> 8 & 255) + "." + (int32 & 255)
// const int32ToIp = (int32) => [int32 >>> 24, int32 >> 16 & 255, int32 >> 8 & 255, int32 & 255].join('.'); 
// const int32ToIp = (int32) => [24, 16, 8, 0].map(e => int32 >> e & 255).join('.');
// const int32ToIp = (int32) => [int32, int32, int32, int32].map((x, i) => ((x >>> (8 * i)) % 256).toString()).reverse().join('.');
const int32ToIp = (int32) => Array(4).fill().map((_, i) => (int32 >>> 8 * i) % 256).reverse().join('.')

// function int32ToIp(int32) {
//     return (((int32 >> 24) & 0xFF) + "." +
//             ((int32 >> 16) & 0xFF) + "." +
//             ((int32 >> 8) & 0xFF) + "." +
//             ((int32) & 0xFF));
// }


q = int32ToIp(2154959208) // "128.114.17.104", "wrong ip for interger: 2154959208"
q
q = int32ToIp(0) // "0.0.0.0", "wrong ip for integer: 0
q
q = int32ToIp(2149583361) // "128.32.10.1", "wrong ip for integer: 2149583361
q