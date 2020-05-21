// 7kyu - Decompose single strand DNA into 3 reading frames

/* In genetics a reading frame is a way to divide a sequence of nucleotides (DNA bases) 
into a set of consecutive non-overlapping triplets (also called codon). 
Each of this triplets is translated into an amino-acid during a translation process to create proteins.

Input: In a single strand of DNA you find 3 Reading frames, take for example the following input sequence:

AGGTGACACCGCAAGCCTTATATTAGC

Output: For the output we are going to take the combinations and show them in the following manner:

Frame 1: AGG TGA CAC CGC AAG CCT TAT ATT AGC
Frame 2: A GGT GAC ACC GCA AGC CTT ATA TTA GC
Frame 3: AG GTG ACA CCG CAA GCC TTA TAT TAG C

For frame 1 split all of them in groups of three starting by the first base (letter).
For frame 2 split all of them in groups of three starting by the second base (letter) but having the first base (letter) at the beggining.
For frame 3 split all of them in groups of three starting by the third letter, but having the first and second bases (letters) at the beginning in the same order. */

// function decomposeSingleStrand(singleStrand) {
//     [frame1, frame2, frame3] = [Array(), Array(), Array()]
//     frame2.push(singleStrand.slice(0, 1))
//     frame3.push(singleStrand.slice(0, 2))
//     for (let i = 0; i < singleStrand.length; i += 3) {
//         frame1.push(singleStrand.slice(i, i+3))
//         frame2.push(singleStrand.slice(i+1, i+4))
//         frame3.push(singleStrand.slice(i+2, i+5))
//     }
//     return `Frame 1: ${frame1.join` `}\nFrame 2: ${frame2.join` `}\nFrame 3: ${frame3.join` `}`
// }

// function decomposeSingleStrand(singleStrand) {
//     let res = ''
//     res += 'Frame 1: ' + singleStrand.match(/.{1,3}/g).join(' ') + '\n'
//     res += 'Frame 2: ' + singleStrand.slice(0, 1) + ' ' + singleStrand.slice(1).match(/.{1,3}/g).join(' ') + '\n'
//     res += 'Frame 3: ' + singleStrand.slice(0, 2) + ' ' + singleStrand.slice(2).match(/.{1,3}/g).join(' ')
//     return res
// }

function decomposeSingleStrand(singleStrand) {
    return [
        `Frame 1: ${singleStrand.match(/.../g).join(' ')}`,
        `Frame 2: ${singleStrand.match(/^.|...|..$/g).join(' ')}`,
        `Frame 3: ${singleStrand.match(/^..|...|.$/g).join(' ')}`,
    ].join('\n');
}

// const decomposeSingleStrand = s => [0, 1, 2].map(i => `Frame ${i+1}: ${(i?[s.slice(0,i)]:[]).concat(s.slice(i).match(/.{1,3}/g)).join(" ")}`).join("\n")


q = decomposeSingleStrand("AGGTGACACCGCAAGCCTTATATTAGC")
// "Frame 1: AGG TGA CAC CGC AAG CCT TAT ATT AGC\nFrame 2: A GGT GAC ACC GCA AGC CTT ATA TTA GC\nFrame 3: AG GTG ACA CCG CAA GCC TTA TAT TAG C")
q