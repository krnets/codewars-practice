/*using System;
using System.Linq;

public class Solution
{
    public static bool solve(String st)
    {
        return Enumerable.Range(0, st.Length / 2)
            .Select(i => Math.Abs(st[i] - st[st.Length - i - 1]))
            .All(x => x == 0 || x == 2);
    }
}*/

/*using System;
using System.Linq;

public class Solution
{
    public static bool solve(String st)
    {
        return st.Reverse()
            .Zip(st, (x, y) => x - y)
            .All(delta => delta == 0 || delta == 2 || delta == -2);
    }
}*/

using System;
using System.Linq;

public class Solution
{
    public static bool solve(String st)
    {
        return st.Take(st.Length / 2)
            .Zip(st.TakeLast(st.Length / 2).Reverse(), (x, y) => Math.Abs(x - y))
            .All(delta => delta == 0 || delta == 2);
    }
}

/*using System;
using System.Linq;

public class Solution
{
    public static bool solve(String st)
    {
        return Enumerable.Range(0, st.Length / 2)
            .Select(i => st[i] - st[st.Length - i - 1])
            .All(x => x == 0 || x == 2 || x == -2);
    }
}*/