using System.Collections.Generic;

public class Kata
{
    public static IEnumerable<int> Delta(IEnumerable<int> enumerable, int n)
    {
        using var iter = (n > 1 ? Delta(enumerable, n - 1) : enumerable).GetEnumerator();

        if (iter.MoveNext() == false)
            yield break;

        var prev = iter.Current;

        while (iter.MoveNext())
        {
            yield return iter.Current - prev;
            prev = iter.Current;
        }
    }
}