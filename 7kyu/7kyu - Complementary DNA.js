// 7kyu - Complementary DNA

// const DNAStrand = dna => [...String(dna)].map(v => v == 'A' ? 'T' : v == 'T' ? 'A' : v == 'G' ? 'C' : v == 'C' ? 'G' : '').join ``

const DNAStrand = dna => dna.replace(/./g, c => 'ACGT' ['TGCA'.indexOf(c)])

q = DNAStrand("AAAA") // "TTTT","String AAAA is"
q
q = DNAStrand("ATTGC") // "TAACG","String ATTGC is"
q
q = DNAStrand("GTAT") // "CATA","String GTAT is"
q