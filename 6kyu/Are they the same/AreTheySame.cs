/*using System;
using System.Linq;

class AreTheySame
{
    public static bool comp(int[] a, int[] b)
    {
        return b != null && a.Sum() == b.Select(v => (int) Math.Sqrt(v)).Sum();
    }
}*/

using System;
using System.Linq;

class AreTheySame
{
    public static bool comp(int[] a, int[] b)
    {
        if (a == null || b == null) return false;

        int[] aSquared = a.Select(v => v * v).OrderBy(v => v).ToArray();
        Array.Sort(b);

        return aSquared.SequenceEqual(b);
    }
}