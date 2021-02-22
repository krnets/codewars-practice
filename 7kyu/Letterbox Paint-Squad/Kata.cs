/*using System.Collections.Generic;
using System.Linq;

public class Kata
{
    public static IEnumerable<int> PaintLetterBoxes(int start, int end)
    {
        var groupBy = string.Concat(Enumerable.Range(start, end - start + 1)).GroupBy(c => c);
        var digits = new int[10];

        foreach (var g in groupBy)
            digits[(int) char.GetNumericValue(g.Key)] = g.Count();
        // digits[g.Key - '0'] = g.Count();

        return digits;
    }
}*/

/*using System.Collections.Generic;
using System.Linq;

public class Kata
{
    public static IEnumerable<int> PaintLetterBoxes(int start, int end)
    {
        var digits = new int[10];

        var map = string.Concat(Enumerable.Range(start, end - start + 1)).GroupBy(c => c)
            .ToDictionary(g => g.Key - '0', g => g.Count());

        foreach (var (key, value) in map)
            digits[key] = value;

        return digits;
    }
}*/

using System.Collections.Generic;

public class Kata
{
    public static IEnumerable<int> PaintLetterBoxes(int start, int end)
    {
        var digits = new int[10];

        for (int i = start; i <= end; i++)
        {
            int n = i;

            while (n > 0)
            {
                digits[n % 10]++;
                n /= 10;
            }
        }

        return digits;
    }
}