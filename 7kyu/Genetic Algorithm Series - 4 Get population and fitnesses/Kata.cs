using System;
using System.Collections.Generic;
using System.Linq;

public class Kata
{
    public IEnumerable<ChromosomeWrap> MapPopulationFit(IEnumerable<string> population, Func<string, double> fitness)
    {
        return population.Select(candidate => new ChromosomeWrap {Chromosome = candidate, Fitness = fitness(candidate)});
    }
}

public class ChromosomeWrap
{
    public string Chromosome { get; set; }
    public double Fitness { get; set; }
}