// 6kyu - Decompose double strand DNA into 6 reading frames

/* In a double strand DNA you find 3 more Reading frames than the single strand DNA reading frames base on the reverse complement-strand.
Input

Given a DNA sequence like the following

AGGTGACACCGCAAGCCTTATATTAGC

Processing

In the reverse complement the following transformations are made

    A-->T
    G-->C
    T-->A
    C-->G

Due to the splicing of DNA strands and the fixed reading direction of a nucleotide strand, the reverse complement gets read from right to left.

DNA                     AGGTGACACCGCAAGCCTTATATTAGC
Reverse complement:     TCCACTGTGGCGTTCGGAATATAATCG  
reversed reverse frame: GCTAATATAAGGCTTGCGGTGTCACCT

You'll have to output:

Frame 1: AGG TGA CAC CGC AAG CCT TAT ATT AGC
Frame 2: A GGT GAC ACC GCA AGC CTT ATA TTA GC
Frame 3: AG GTG ACA CCG CAA GCC TTA TAT TAG C

Reverse Frame 1: GCT AAT ATA AGG CTT GCG GTG TCA CCT
Reverse Frame 2: G CTA ATA TAA GGC TTG CGG TGT CAC CT
Reverse Frame 3: GC TAA TAT AAG GCT TGC GGT GTC ACC T

Instructions on how to output the first 3 frames are on a previous simpler kata Decompose single strand DNA into 3 reading frames */

// function decomposeDoubleStrand(singleStrand) {
//     let rev = [...singleStrand.replace(/[AGTC]/g, m => ({ A:'T', G:'C', T:'A', C:'G' })[m])].reverse().join('')
//     return [[
//             `Frame 1: ${singleStrand.match(/.../g).join(' ')}`,
//             `Frame 2: ${singleStrand.match(/^.|...|..$/g).join(' ')}`,
//             `Frame 3: ${singleStrand.match(/^..|...|.$/g).join(' ')}`,
//         ].join('\n'),[
//             `Reverse Frame 1: ${rev.match(/.../g).join(' ')}`,
//             `Reverse Frame 2: ${rev.match(/^.|...|..$/g).join(' ')}`,
//             `Reverse Frame 3: ${rev.match(/^..|...|.$/g).join(' ')}`,
//         ].join('\n')].join('\n\n')
// }

function decomposeDoubleStrand(singleStrand) {
    let rev = [...singleStrand].map(m => ({ A:'T', G:'C', T:'A', C:'G' })[m]).reverse().join('')
    return [
            `Frame 1: ${singleStrand.match(/.../g).join(' ')}`,
            `Frame 2: ${singleStrand.match(/^.|...|..$/g).join(' ')}`,
            `Frame 3: ${singleStrand.match(/^..|...|.$/g).join(' ')}`,
        '',
            `Reverse Frame 1: ${rev.match(/.../g).join(' ')}`,
            `Reverse Frame 2: ${rev.match(/^.|...|..$/g).join(' ')}`,
            `Reverse Frame 3: ${rev.match(/^..|...|.$/g).join(' ')}`,
        ].join('\n')
}


q = decomposeDoubleStrand("AGGTGACACCGCAAGCCTTATATTAGC")
// "Frame 1: AGG TGA CAC CGC AAG CCT TAT ATT AGC\nFrame 2: A GGT GAC ACC GCA AGC CTT ATA TTA GC\nFrame 3: AG GTG ACA CCG CAA GCC TTA TAT TAG C\n
// \nReverse Frame 1: GCT AAT ATA AGG CTT GCG GTG TCA CCT\nReverse Frame 2: G CTA ATA TAA GGC TTG CGG TGT CAC CT\nReverse Frame 3: GC TAA TAT AAG GCT TGC GGT GTC ACC T")                      
q
