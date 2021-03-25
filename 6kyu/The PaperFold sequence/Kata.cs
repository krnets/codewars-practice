/*
using System.Collections.Generic;

public class Kata
{
    public static IEnumerable<int> PaperFold()
    {
        for (int i = 1;; i++)
        {
            int p = i;
            int q = p & -p;

            p = p & (q << 1);

            yield return p == 0 ? 1 : 0;
        }
    }
}
*/

using System.Collections.Generic;

public class Kata
{
    public static IEnumerable<int> PaperFold()
    {
        var enumerator = PaperFold().GetEnumerator();

        for (var i = 0; i < int.MaxValue; i++)
        {
            yield return 1;
            enumerator.MoveNext();

            yield return enumerator.Current;
            yield return 0;

            enumerator.MoveNext();
            yield return enumerator.Current;
        }
    }
}