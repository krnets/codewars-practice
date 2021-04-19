/*using System.Collections.Generic;
using System.Linq;

public class Kata
{
    public static bool IsBalanced(string s, string caps)
    {
        s = string.Concat(s.Where(caps.Contains));

        if (s.Length % 2 != 0)
            return false;

        var pairs = Enumerable.Range(0, caps.Length / 2).ToDictionary(i => caps[2 * i], i => caps[2 * i + 1]);
        var stack = new Stack<char>();

        foreach (var c in s)
        {
            if (pairs.ContainsKey(c))
                stack.Push(c);

            else if (pairs[stack.Peek()] == c)
                stack.Pop();

            else return false;
        }

        return true;
    }
}*/


using System.Collections.Generic;
using System.Linq;

public class Kata
{
    public static bool IsBalanced(string s, string caps)
    {
        var pairs = Enumerable.Range(0, caps.Length / 2).ToDictionary(i => caps[2 * i], i => caps[2 * i + 1]);
        var stack = new Stack<char>();

        foreach (var c in s.Where(caps.Contains))
            if (pairs.ContainsValue(c) && stack.Count > 0 && pairs[stack.Peek()] == c)
                stack.Pop();

            else if (pairs.ContainsKey(c))
                stack.Push(c);

            else return false;

        return stack.Count == 0;
    }
}