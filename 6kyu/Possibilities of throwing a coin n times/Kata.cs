/*using System;
using System.Collections.Generic;
using System.Linq;

public class Kata
{
    public List<string> coin(int n)
    {
        return Enumerable.Range(0, (int) Math.Pow(2, n))
            .Select(i => string.Concat(Convert.ToString(i, 2).PadLeft(n, '0').Select(c => c == '0' ? 'H' : 'T')))
            .ToList();
    }
}*/

using System.Collections.Generic;
using System.Linq;

public class Kata
{
    public List<string> coin(int n)
    {
        var list = new List<string> {"H", "T"};

        for (int i = 1; i < n; i++)
            list = list.Select(s => $"H{s}").Union(list.Select(s => $"T{s}")).ToList();

        return list;
    }
}