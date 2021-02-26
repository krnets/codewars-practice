### Genetic Algorithm Series - #4 Get population and fitnesses

In a genetic algorithm, a population is a collection of candidates that may evolve toward a better solution.

We determine how close a chromosome is to a ideal solution by calculating its fitness. 
You are given two parameters, the population containing all individuals and a function fitness that determines how close to the solution a chromosome is.

Your task is to return a collection containing an object with the chromosome and the calculated fitness.

[
  { chromosome: c, fitness: f },
  { chromosome: c, fitness: f },
  ...
]

Note: you have a pre-loaded class ChromosomeWrap and you should return a collection of it instead.
```c#
public class ChromosomeWrap
{
    public string Chromosome { get; set; }
    public double Fitness { get; set; }
}