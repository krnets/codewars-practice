/*using System.Collections.Generic;
using System.Linq;
using System.Text;

public class Kata
{
    public int DeleteDigit(int n)
    {
        var numStr = n.ToString();
        var list = new List<string>();

        for (int i = 0; i < numStr.Length; i++)
        {
            var sb = new StringBuilder().Append(numStr);
            sb.Remove(i, 1);
            list.Add(sb.ToString());
        }

        return list.Max(int.Parse);
    }
}*/

/*using System;
using System.Linq;
using System.Text;

public class Kata
{
    public int DeleteDigit(int n)
    {
        return Enumerable.Range(0, (int) (Math.Log10(n) + 1))
            .Select(i =>
            {
                var sb = new StringBuilder().Append(n.ToString());
                sb.Remove(i, 1);
                return sb.ToString();
            })
            .Max(int.Parse);
    }
}*/

using System.Linq;

public class Kata
{
    public int DeleteDigit(int n)
    {
        var numStr = n.ToString();

        return numStr.Select((_, i) => numStr.Remove(i, 1)).Max(int.Parse);
    }
}