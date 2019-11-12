// 7kyu - The Office III - Broken Photocopier

// const broken = x => [...x].map(v => (v == '1') ? '0' : (v == '0') ? '1' : '').join``
// const broken = x => [...x].map(d => Number(d) ^ 1).join ``
// const broken = x => [...x].map(d => +d ^ 1).join ``
// const broken = x => [...x].map(d => d ^ 1).join ``
// const broken = x => [...x].map(d => 1 - d).join ``

// const broken = x => x.replace(/[10]/g, d => +d ? 0 : 1)
// const broken = x => x.replace(/./g, d => +!+d)
// const broken = x => x.replace(/./g, d => +d ^ 1)
// const broken = x => x.replace(/./g, n => n ^ 1)
// const broken = x => x.replace(/[01]/g, n => 1 - n)
// const broken = x => x.replace(/./g, b => '01' ['10'.indexOf(b)])
const broken = x => x.replace(/[01]/g, bit => '10'[bit])

q = broken("1") // "0"
q
q = broken("10000000101101111110011001000") // "01111111010010000001100110111"
q
q = broken("100010") // "011101"
q