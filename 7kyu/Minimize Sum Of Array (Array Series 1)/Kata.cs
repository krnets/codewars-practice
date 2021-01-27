using System;

class Kata
{
    public static int MinSum(int[] a)
    {
        Array.Sort(a);
        int sum = 0;

        for (int i = 0; i < a.Length - i - 1; i++)
        // for (int i = 0; i < a.Length / 2; i++)
            sum += a[i] * a[a.Length - i - 1];

        return sum;
    }
}

/*using System;
using System.Linq;

class Kata
{
    public static int MinSum(int[] a)
    {
        Array.Sort(a);

        return Enumerable.Range(0, a.Length / 2)
            .Sum(i => a[i] * a[a.Length - i - 1]);
    }
}*/