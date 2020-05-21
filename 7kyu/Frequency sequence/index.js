// 7kyu - Frequency sequence

// function freqSeq(str, sep) {
//     let count = [...str].reduce((freq, char) => (freq[char] = ++freq[char] || 1, freq), {})
//     return [...str].map(v => count[v]).join(sep)
// }

// const freqSeq = (str, sep) => [...str].map(v => [...str].reduce((freq, char) => (freq[char] = ++freq[char] || 1, freq), {})[v]).join(sep)

// const freqSeq = (str, sep) => [...str].map((v, i, a) => a.filter(vi => vi == v).length).join(sep)

const freqSeq = (str, sep) => [...str].map(v => str.split(v).length - 1).join(sep)


q = freqSeq('hello world', '-') // '1-1-3-3-2-1-1-2-1-3-1'
q
q = freqSeq('19999999', ':') // '1:7:7:7:7:7:7:7'
q
q = freqSeq('^^^**$', 'x') // '3x3x3x2x2x1'
q