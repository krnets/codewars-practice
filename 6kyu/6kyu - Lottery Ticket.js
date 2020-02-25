// 6kyu - Lottery Ticket

/* Given a lottery ticket (ticket), represented by an array of 2-value arrays, you must find out if you've won the jackpot. 
Example ticket:

[ [ 'ABC', 65 ], [ 'HGR', 74 ], [ 'BYHT', 74 ] ]

To do this, you must first count the 'mini-wins' on your ticket. Each sub array has both a string and a number within it. 
If the character code of any of the characters in the string matches the number, you get a mini win. 
Note you can only have one mini win per sub array.

Once you have counted all of your mini wins, compare that number to the other input provided (win). 
If your total is more than or equal to (win), return 'Winner!'. Else return 'Loser!'.

All inputs will be in the correct format. Strings on tickets are not always the same length. */

// const bingo = (ticket, win) => [...ticket].map(v => [...v[0]].map(c => c.charCodeAt()).some(x => x == v[1])).filter(Boolean).length >= win ? 'Winner!' : 'Loser!'
const bingo = (ticket, win) => [...ticket].map(v => v[0].includes(String.fromCharCode(v[1]))).filter(Boolean).length >= win ? 'Winner!' : 'Loser!'

q = bingo([['DDNORVH',71],['QBDYVE',74],['NIVQNMOT',72],['IZOSZD',90],['WDIS',81],['MDSEIELN',69],['OU',90],['AODBXW',84],['NYMEAIEV',82]], 1)
q
q = bingo([['ABC', 65], ['HGR', 74], ['BYHT', 74]], 2) // 'Loser!'
q
q = bingo([['ABC', 65], ['HGR', 74], ['BYHT', 74]], 1) // 'Winner!'
q
q = bingo([['HGTYRE', 74], ['BE', 66], ['JKTY', 74]], 3) // 'Loser!'
q