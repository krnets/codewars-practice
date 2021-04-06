/*using System.Collections.Generic;
using System.Linq;
using static System.String;

public class PrimeDecomp
{
    public static string factors(int n)
    {
        var factors = new List<int>();
        var divisor = 2;

        while (n != 1)
        {
            while (n % divisor == 0)
            {
                n /= divisor;
                factors.Add(divisor);
            }

            divisor++;
        }

        return Concat(factors.GroupBy(i => i).Select(g => g.Count() > 1 ? $"({g.Key}**{g.Count()})" : $"({g.Key})"));
    }
}*/

using System.Collections.Generic;
using System.Linq;
using static System.String;

public class PrimeDecomp
{
    public static string factors(int n)
    {
        var factors = new List<int>();

        for (int divisor = 2; n != 1; divisor++)
        {
            while (n % divisor == 0)
            {
                n /= divisor;
                factors.Add(divisor);
            }
        }

        return Concat(factors.GroupBy(i => i).Select(g => g.Count() > 1 ? $"({g.Key}**{g.Count()})" : $"({g.Key})"));
    }
}