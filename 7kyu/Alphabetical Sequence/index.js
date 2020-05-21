// 7kyu - Alphabetical Sequence

/* In this kata you will be given a random string of letters and tasked with returning them as a string 
of comma-separated sequences sorted alphabetcally, with each sequence starting with an uppercase character 
followed by n-1 lowercase characters, where n is the letter's alphabet position 1-26.

alphaSeq("ZpglnRxqenU") -> "Eeeee,Ggggggg,Llllllllllll,Nnnnnnnnnnnnnn,Nnnnnnnnnnnnnn,Pppppppppppppppp,Qqqqqqqqqqqqqqqqq,Rrrrrrrrrrrrrrrrrr,Uuuuuuuuuuuuuuuuuuuuu,Xxxxxxxxxxxxxxxxxxxxxxxx,Zzzzzzzzzzzzzzzzzzzzzzzzzz"

    The string will include only letters.
    The first letter of each sequence is uppercase followed by n-1 lowercase.
    Each sequence is seperated with a comma.
    Return value needs to be a string. */

// function alphaSeq(str) {
//     return [...str.toLowerCase()]
//         .map(v => v.repeat(v.charCodeAt() - 96))
//         .sort((a, b) => a.length - b.length)
//         .map(v => v[0].toUpperCase() + v.slice(1))
//         .toString()
// }

const alphaSeq = (str) => [...str.toLowerCase()].sort().map(v => v.toUpperCase() + v.repeat(v.charCodeAt() - 97)).toString()

q = alphaSeq("qenU")
q
// Eeeee,Nnnnnnnnnnnnnn,Qqqqqqqqqqqqqqqqq,Uuuuuuuuuuuuuuuuuuuuu
q = alphaSeq("ZpglnRxqenU")
q
// "Eeeee,Ggggggg,Llllllllllll,Nnnnnnnnnnnnnn,Nnnnnnnnnnnnnn,Pppppppppppppppp,Qqqqqqqqqqqqqqqqq,Rrrrrrrrrrrrrrrrrr,Uuuuuuuuuuuuuuuuuuuuu,Xxxxxxxxxxxxxxxxxxxxxxxx,Zzzzzzzzzzzzzzzzzzzzzzzzzz"
q = alphaSeq("NyffsGeyylB")
q
// "Bb,Eeeee,Ffffff,Ffffff,Ggggggg,Llllllllllll,Nnnnnnnnnnnnnn,Sssssssssssssssssss,Yyyyyyyyyyyyyyyyyyyyyyyyy,Yyyyyyyyyyyyyyyyyyyyyyyyy,Yyyyyyyyyyyyyyyyyyyyyyyyy"
q = alphaSeq("MjtkuBovqrU")
q
// "Bb,Jjjjjjjjjj,Kkkkkkkkkkk,Mmmmmmmmmmmmm,Ooooooooooooooo,Qqqqqqqqqqqqqqqqq,Rrrrrrrrrrrrrrrrrr,Tttttttttttttttttttt,Uuuuuuuuuuuuuuuuuuuuu,Uuuuuuuuuuuuuuuuuuuuu,Vvvvvvvvvvvvvvvvvvvvvv"
q = alphaSeq("EvidjUnokmM")
q
// "Dddd,Eeeee,Iiiiiiiii,Jjjjjjjjjj,Kkkkkkkkkkk,Mmmmmmmmmmmmm,Mmmmmmmmmmmmm,Nnnnnnnnnnnnnn,Ooooooooooooooo,Uuuuuuuuuuuuuuuuuuuuu,Vvvvvvvvvvvvvvvvvvvvvv"
q = alphaSeq("HbideVbxncC")
q
// "Bb,Bb,Ccc,Ccc,Dddd,Eeeee,Hhhhhhhh,Iiiiiiiii,Nnnnnnnnnnnnnn,Vvvvvvvvvvvvvvvvvvvvvv,Xxxxxxxxxxxxxxxxxxxxxxxx"