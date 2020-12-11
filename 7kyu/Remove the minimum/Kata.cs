/*using System.Collections.Generic;
using System.Linq;

public class Remover
{
    public static List<int> RemoveSmallest(List<int> numbers)
    {
        if (numbers.Count == 0) return numbers;

        int min = numbers.Min();
        List<int> clone = numbers;
        clone.Remove(min);

        return clone;
    }
}*/

using System.Collections.Generic;
using System.Linq;

public class Remover
{
    public static List<int> RemoveSmallest(List<int> numbers)
    {
        if (numbers.Count == 0)
            return numbers;

        int min = numbers.Min();
        int indexMin = numbers.IndexOf(min);

        return numbers.Where((_, i) => i != indexMin).ToList();
    }
}