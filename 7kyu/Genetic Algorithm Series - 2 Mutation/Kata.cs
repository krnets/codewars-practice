/*using System;
using System.Text;

public class Kata
{
    public string Mutate(string chromosome, double probability)
    {
        var sb = new StringBuilder();
        var rnd = new Random();

        foreach (char c in chromosome)
        {
            if (c == '0')
                sb.Append(rnd.NextDouble() < probability ? 1 : 0);
            else if (c == '1')
                sb.Append(rnd.NextDouble() < probability ? 0 : 1);
        }

        return sb.ToString();
    }
}*/

using System;
using System.Linq;

public class Kata
{
    private Random rnd = new Random();

    public string Mutate(string chromosome, double probability)
    {
        return string.Concat(chromosome.Select(c => rnd.NextDouble() < probability ? (c == '0' ? '1' : '0') : c));
    }
}