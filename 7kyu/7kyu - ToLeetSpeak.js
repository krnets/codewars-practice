// 7kyu - ToLeetSpeak

// const toLeetSpeak = str => [...str].map(c => c == 'A' ? '@' :
//                                              c == 'B' ? '8' :
//                                              c == 'C' ? '(' :
//                                              c == 'E' ? '3' :
//                                              c == 'G' ? '6' :
//                                              c == 'H' ? '#' :
//                                              c == 'I' ? '!' :
//                                              c == 'L' ? '1' :
//                                              c == 'O' ? '0' :
//                                              c == 'S' ? '$' :
//                                              c == 'T' ? '7' :
//                                              c == 'Z' ? '2' :
//                                              c).join``

// const toLeetSpeak = str => [...str].map(c => '@8(D3F6#!JK1MN0PQR$7UVWXY2'[c.charCodeAt() - 65] || c).join``

const toLeetSpeak = str => str.replace(/[ABCEGHILOSTZ]/g, c => '@8(36#!10$72'['ABCEGHILOSTZ'.indexOf(c)])

// const toLeetSpeak = s => s.replace(/./g, c => ({A:'@',B:8,C:'(',E:3,G:6,H:'#',I:'!',L:'1',O:'0',S:'$',T:7,Z:2})[c] || c)


q = toLeetSpeak("LEET"), "1337"
q
q = toLeetSpeak("CODEWARS"), "(0D3W@R$"
q
q = toLeetSpeak("HELLO WORLD"), "#3110 W0R1D"
q
q = toLeetSpeak("LOREM IPSUM DOLOR SIT AMET"), "10R3M !P$UM D010R $!7 @M37"
q
q = toLeetSpeak("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"), "7#3 QU!(K 8R0WN F0X JUMP$ 0V3R 7#3 1@2Y D06"
q