/*using System.Collections.Generic;
using System.Linq;

public static class Kata
{
    public static IEnumerable<T> UniqueInOrder<T>(IEnumerable<T> iterable)
    {
        if (!iterable.Any()) return iterable;

        var list = new List<T>();
        T previous = iterable.First();

        foreach (T element in iterable)
        {
            if (!previous.Equals(element) || list.Count == 0)
                list.Add(element);

            previous = element;
        }

        return list;
    }
}*/

using System.Collections.Generic;
using System.Linq;

public static class Kata
{
    public static IEnumerable<T> UniqueInOrder<T>(IEnumerable<T> iterable)
    {
        return iterable.Where((v, i) => i == 0 || !v.Equals(iterable.ElementAt(i - 1)));
    }
}