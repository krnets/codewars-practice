// const DNAtoRNA = dna => dna.replace(/T/gi, 'U')
const DNAtoRNA = dna => dna.split('T').join('U')

q = DNAtoRNA("TTTT") // "UUUU")
q
q = DNAtoRNA("GCAT") // "GCAU")
q
q = DNAtoRNA("GACCGCCGCC") // "GACCGCCGCC")
q