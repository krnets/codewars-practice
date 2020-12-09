/*using System;
using System.Collections.Generic;
using System.Linq;

public class Accumul
{
    public static String Accum(string s)
    {
        var list = new List<string>();

        for (int i = 0; i < s.Length; i++)
        {
            var head = char.ToUpper(s[i]);
            var tail = string.Concat(Enumerable.Repeat(s[i], i)).ToLower();

            list.Add(head + tail);
        }

        return String.Join("-", list);
    }
}*/

using System;
using System.Linq;

public class Accumul
{
    public static String Accum(string s)
    {
        return string.Join("-", s.ToLower().Select((c, i) => char.ToUpper(c) + new string(c, i)));
    }
}