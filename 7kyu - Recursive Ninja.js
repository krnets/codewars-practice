// 7kyu - Recursive Ninja

const chirp = n => n > 1 ? chirp(n - 1) + '-chirp' : 'chirp'

q = chirp(4) // "chirp-chirp-chirp-chirp"
q
q = chirp(2) // "chirp-chirp"
q