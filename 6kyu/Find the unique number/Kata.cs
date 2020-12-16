using System.Collections.Generic;
using System.Linq;

public class Kata
{
    public static int GetUnique(IEnumerable<int> numbers)
    {
        return numbers.GroupBy(x => x).Single(g => g.Count() == 1).Key;
    }
}