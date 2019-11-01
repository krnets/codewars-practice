// const accum = s => [...s].map((v, i) => v.repeat(i + 1)).map(v => v.slice(0, 1).toUpperCase() + v.slice(1).toLowerCase()).join('-')
const accum = s => [...s].map((char, index) => (char.toUpperCase() + char.toLowerCase().repeat(index))).join`-`
const repeat = (s, n) => Array.from({length: n}, () => s).join("")

q = repeat('a', 5)
q
q = accum("ZpglnRxqenU") // "Z-Pp-Ggg-Llll-Nnnnn-Rrrrrr-Xxxxxxx-Qqqqqqqq-Eeeeeeeee-Nnnnnnnnnn-Uuuuuuuuuuu"
q
q = accum("NyffsGeyylB") // "N-Yy-Fff-Ffff-Sssss-Gggggg-Eeeeeee-Yyyyyyyy-Yyyyyyyyy-Llllllllll-Bbbbbbbbbbb"
q
q = accum("MjtkuBovqrU") // "M-Jj-Ttt-Kkkk-Uuuuu-Bbbbbb-Ooooooo-Vvvvvvvv-Qqqqqqqqq-Rrrrrrrrrr-Uuuuuuuuuuu"
q
q = accum("EvidjUnokmM") // "E-Vv-Iii-Dddd-Jjjjj-Uuuuuu-Nnnnnnn-Oooooooo-Kkkkkkkkk-Mmmmmmmmmm-Mmmmmmmmmmm"
q
q = accum("HbideVbxncC") // "H-Bb-Iii-Dddd-Eeeee-Vvvvvv-Bbbbbbb-Xxxxxxxx-Nnnnnnnnn-Cccccccccc-Ccccccccccc"
q