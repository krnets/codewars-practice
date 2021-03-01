/*using System.Collections.Generic;

public class Kata
{
    public IEnumerable<string> Crossover(string chromosome1, string chromosome2, int cut)
    {
        var resultChromosome1 = chromosome1[..cut] + chromosome2[cut..];
        var resultChromosome2 = chromosome2[..cut] + chromosome1[cut..];

        return new List<string>() {resultChromosome1, resultChromosome2};
    }
}*/

using System.Collections.Generic;

public class Kata
{
    public IEnumerable<string> Crossover(string chromosome1, string chromosome2, int cut)
    {
        yield return chromosome1[..cut] + chromosome2[cut..];
        yield return chromosome2[..cut] + chromosome1[cut..];
    }
}