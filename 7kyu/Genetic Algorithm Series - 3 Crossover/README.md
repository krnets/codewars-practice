### Genetic Algorithm Series - #3 Crossover

In genetic algorithms, crossover is a genetic operator used to vary the programming of chromosomes from one generation to the next.

The one-point crossover consists in swapping one's cromosome part with another in a specific given point. 

The image bellow shows the crossover being applied on chromosomes 1011011001111 and 1011100100110 with the cut point (index) 4:

![Crossover](https://i.imgur.com/nZ4hgnS.gif)

In this kata you have to implement a function crossover that receives two chromosomes chromosome1, chromosome2 and a zero-based index and it has to return an array with the crossover result on both chromosomes [chromosome1, chromosome2].

Example:

crossover('111000', '000110', 3) should return ['111110', 000000']
