// 8kyu - training js #14: methods of number object--tostring() and tolocalestring()

// const colorOf = (r, g, b) => '#' + [r, g, b].map((v => v.toString(16).padStart(2, 0))).join ``
// const colorOf = (r, g, b) => '#' + [r, g, b].map((v => v.toString(16).replace(/^(.)$/, '0$1'))).join``
const colorOf = (...rgb) => '#' + rgb.map(v => v.toString(16).padStart(2, 0)).join ``
// const colorOf = (...rgb) => '#' + rgb.map(v => (0 + v.toString(16)).slice(-2)).join ``


q = colorOf(255, 0, 0) // "#ff0000"
q
q = colorOf(0, 111, 0) // "#006f00"
q
q = colorOf(1, 2, 3) // "#010203"
q