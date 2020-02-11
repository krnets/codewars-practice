// 7kyu - Alphabet war

/* There is a war and nobody knows - the alphabet war! There are two groups of hostile letters. 
The tension between left side letters and right side letters was too high and the war began.

Write a function that accepts fight string consists of only small letters and return who wins the fight. 
When the left side wins return Left side wins!, when the right side wins return Right side wins!, 
in other case return Let's fight again!.

The left side letters and their power:

 w - 4
 p - 3
 b - 2
 s - 1

The right side letters and their power:

 m - 4
 q - 3
 d - 2
 z - 1

The other letters don't have power and are only victims. */

// function alphabetWar(fight) {
//     let leftLetterPower = { w: 4, p: 3, b: 2, s: 1 }
//     let rightLetterPower = { m: 4, q: 3, d: 2, z: 1 }
//     let left = [...fight].map(v => leftLetterPower[v]).filter(Boolean).reduce((a, b) => a + b, 0)
//     let right = [...fight].map(v => rightLetterPower[v]).filter(Boolean).reduce((a, b) => a + b, 0)
//     return left > right ? "Left side wins!" : left < right ? "Right side wins!" : "Let's fight again!"
// }

// function alphabetWar(fight) {
//     let score = [...fight].reduce((acc, v) => acc + 'sbpw'.indexOf(v) - 'zdqm'.indexOf(v), 0)
//     return score == 0 ? "Let's fight again!" : `${score > 0 ? 'Left' : 'Right'} side wins!`
// }

const alphabetWar = (fight) => ["Right side wins!", "Let's fight again!", "Left side wins!"]
                               [Math.sign([...fight].reduce((acc, v) => acc + 'sbpw'.indexOf(v) - 'zdqm'.indexOf(v), 0)) + 1]

q = alphabetWar("z"); //=> Right side wins
q
q = alphabetWar("zdqmwpbs"); //=> Let's fight again
q
q = alphabetWar("zzzzs"); //=> Right side wins
q
q = alphabetWar("wwwwwwz"); //=> Left side wins!
q
q = alphabetWar("aqpyux") // Let's fight again!
q