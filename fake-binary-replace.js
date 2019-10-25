// const fakeBin = (x) => x.split('').map((value, index) => value < 5 ? 0 : 1).join('')
const fakeBin = (x) => x.replace(/\d/g, v => v < 5 ? 0 : 1)

q = fakeBin('45385593107843568') // '01011110001100111'
q
q = fakeBin('509321967506747') // '101000111101101'
q
q = fakeBin('366058562030849490134388085') // '011011110000101010000011011'
q