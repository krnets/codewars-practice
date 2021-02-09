/*using System.Collections.Generic;
using System.Linq;

public class Consecutives
{
    public static List<int> SumConsecutives(List<int> s)
    {
        int prev = default;
        var stack = new Stack<int>();

        foreach (var i in s)
            if (i == prev)
                stack.Push(stack.Pop() + prev);
            else
            {
                stack.Push(i);
                prev = i;
            }

        return stack.Reverse().ToList();
    }
}*/

/*
using System.Collections.Generic;
using System.Linq;

public class Consecutives
{
    public static List<int> SumConsecutives(List<int> s)
    {
        var stack = new Stack<int>(new[] {s[0]});

        for (int i = 1; i < s.Count; i++)
        {
            var acc = s[i];

            if (s[i - 1] == s[i])
                acc += stack.Pop();

            stack.Push(acc);
        }

        return stack.Reverse().ToList();
    }
}
*/

/*using System.Collections.Generic;
using System.Linq;

public class Consecutives
{
    public static List<int> SumConsecutives(List<int> s)
    {
        return s.Select((v, i) =>
                (i > 0 && s[i - 1] == v) ? (int?) null : s.Skip(i).TakeWhile(t => t == v).Sum())
            .Where(r => r.HasValue)
            .Select(r => r.Value)
            .ToList();
    }
}*/

using System.Collections.Generic;
using System.Linq;

public class Consecutives
{
    public static List<int> SumConsecutives(List<int> s)
    {
        return s.Select((val, i) => (val, i))
            .Where(tuple => tuple.i == 0 || s[tuple.i - 1] != tuple.val)
            .Select(tuple => s.Skip(tuple.i)
                .TakeWhile(x => tuple.val == x)
                .Sum())
            .ToList();
    }
}