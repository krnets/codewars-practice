/*using System.Linq;
using System.Collections.Generic;

public static class Kata
{
    public static int[] ArrayLeaders(int[] numbers)
    {
        var list = new LinkedList<int>();

        for (int i = numbers.Length - 1; i >= 0; i--)
            if (numbers[i] > numbers.Skip(i + 1).Sum())
                list.AddFirst(numbers[i]);

        return list.ToArray();
    }
}*/

/*using System.Collections.Generic;
using System.Linq;

public static class Kata
{
    public static int[] ArrayLeaders(int[] numbers)
    {
        var list = new List<int>();

        for (int i = 0; i < numbers.Length; i++)
            if (numbers[i] > numbers.Skip(i + 1).Sum())
                list.Add(numbers[i]);

        return list.ToArray();
    }
}*/

/*using System.Linq;

public static class Kata
{
    public static int[] ArrayLeaders(int[] numbers)
    {
        return Enumerable.Range(0, numbers.Length)
            .Where(i => numbers[i] > numbers.Skip(i + 1).Sum())
            .Select(i => numbers[i])
            .ToArray();
    }
}*/

using System.Linq;

public static class Kata
{
    public static int[] ArrayLeaders(int[] numbers)
    {
        return numbers.Where((x, i) => x > numbers.Skip(i + 1).Sum()).ToArray();
    }
}