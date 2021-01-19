/*using System;
using System.Collections.Generic;

public class SequenceSum
{
    public static int[] SumOfN(int n)
    {
        int sum = 0;
        var list = new List<int>(sum);
        bool negative = n < 0;

        for (int i = 0; i <= Math.Abs(n); i++)
        {
            sum += i;
            list.Add(negative ? -sum : sum);
        }

        return list.ToArray();
    }
}
*/

/*using System;
using System.Linq;

public class SequenceSum
{
    public static int[] SumOfN(int n)
    {
        return Enumerable.Range(0, Math.Abs(n) + 1)
                         .Select(i => Math.Sign(n) * i * (i + 1) / 2)
                         .ToArray();
    }
}*/
/*using System;
using System.Collections.Generic;
using System.Linq;

public class SequenceSum
{
    public static int[] SumOfN(int n)
    {
        int sum = 0;
        var list = new List<int>();

        for (int i = 0; i <= Math.Abs(n); i++)
        {
            sum += i;
            list.Add(sum);
        }

        return (n < 0) ? list.Select(i => -i).ToArray() : list.ToArray();
    }
}
*/
using System;

public class SequenceSum
{
    public static int[] SumOfN(int n)
    {
        var sequence = new int[Math.Abs(n) + 1];

        for (int i = 0; i <= Math.Abs(n); i++)
            sequence[i] = i * (i + 1) / 2 * Math.Sign(n);

        return sequence;
    }
}