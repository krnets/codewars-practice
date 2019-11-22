// 6kyu - Data Reverse

/* A stream of data is received and needs to be reversed.
Each segment is 8 bits long, meaning the order of these segments needs to be reversed, for example:

11111111  00000000  00001111  10101010
 (byte1)   (byte2)   (byte3)   (byte4)

should become:

10101010  00001111  00000000  11111111
 (byte4)   (byte3)   (byte2)   (byte1)

The total number of bits will always be a multiple of 8.
The data is given in an array as such:

[1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0] */

// function dataReverse(data) {
//     let segments = []
//     for (let i = 0; i < data.length; i += 8)
//         segments.push(data.slice(i, i + 8))
//     return segments.reverse().reduce((a, b) => a.concat(b), [])
// }

// const dataReverse = data => data.join``.match(/\d{8}/g).reverse().join``.split``.map(Number)

// function dataReverse(data) {
//     let bytes = []
//     for (let i = 0; i < data.length; i += 8) 
//       bytes.unshift(...data.slice(i, i + 8))
//     return bytes
// }

function dataReverse(data) {
    let a = [];
    while (data.length)
        a.unshift(...data.splice(0, 8));
    return a;
}

const data1 = [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0]
q = dataReverse(data1)
//  [1,0,1,0,1,0,1,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1]
q

const data3 = [0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1]
q = dataReverse(data3)
//  [0,0,1,0,1,0,0,1,0,0,1,1,0,1,1,0]
q
