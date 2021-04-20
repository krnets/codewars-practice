/*
using System.Collections.Generic;
using System.Linq;

public class Kata
{
    public List<string> Possibilities(string input)
    {
        int i = input.IndexOf('?');

        if (i < 0) return new List<string> {input};

        var list0 = Possibilities(input[..i] + "0" + input[(i + 1)..]);
        var list1 = Possibilities(input[..i] + "1" + input[(i + 1)..]);

        return list0.Concat(list1).ToList();
    }
}
*/


using System.Collections.Generic;
using System.Linq;
using System;

public class Kata
{
    public List<string> Possibilities(string s)
    {
        var arr = s.Split('?');
        int n = 1 << s.Count(c => c == '?');

        return Enumerable.Range(n, n)
            .Select(i => string.Concat(arr.Zip(Convert.ToString(i, 2), (str, c) => c + str))[1..])
            .ToList();
    }
}