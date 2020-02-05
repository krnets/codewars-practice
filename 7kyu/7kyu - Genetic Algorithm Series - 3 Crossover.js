// 7kyu - Genetic Algorithm Series - #3 Crossover

/* In genetic algorithms, crossover is a genetic operator used to vary the programming of chromosomes 
from one generation to the next.

The one-point crossover consists in swapping one's cromosome part with another in a specific given point. 

In this kata you have to implement a function crossover that receives two chromosomes chromosome1, chromosome2 
and a zero-based index and it has to return an array with the crossover result on both chromosomes [chromosome1, chromosome2].

crossover('111000', '000110', 3) should return ['111110', 000000'] */

// function crossover(chromosome1, chromosome2, index) {
//     let cut1 = chromosome1.slice(index)
//     let cut2 = chromosome2.slice(index)
//     return [chromosome1.slice(0, index) + cut2, chromosome2.slice(0, index) + cut1]
// };

function crossover(chromosome1, chromosome2, index) {
    return [
        chromosome1.slice(0, index) + chromosome2.slice(index),
        chromosome2.slice(0, index) + chromosome1.slice(index)
    ]
}

q = crossover('111000', '000110', 3) // ['111110', '000000']
q
q = crossover('110', '001', 2)[0] // '111'
q
q = crossover('110', '001', 2)[1] // '000'
q
q = crossover('111000', '000110', 3)[0] // '111110'
q
q = crossover('111000', '000110', 3)[1] // '000000'
q