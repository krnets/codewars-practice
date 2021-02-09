/*using System.Text;

public class Kata
{
    public static string CleanString(string s)
    {
        var sb = new StringBuilder();

        foreach (char c in s)
        {
            if (c == '#' && sb.Length == 0)
                continue;
            if (c == '#' && sb.Length > 0)
                sb.Remove(sb.Length - 1, 1);
            else
                sb.Append(c);
        }

        return sb.ToString();
    }
}*/

/*using System.Text;

public class Kata
{
    public static string CleanString(string s)
    {
        var sb = new StringBuilder();

        foreach (char c in s)
        {
            if (c == '#')
            {
                if (sb.Length > 0)
                    sb.Remove(sb.Length - 1, 1);
            }
            else
                sb.Append(c);
        }

        return sb.ToString();
    }
}*/

using System.Collections.Generic;
using System.Linq;

public class Kata
{
    public static string CleanString(string s)
    {
        var stack = new Stack<char>();

        foreach (char c in s)
            if (c == '#')
                stack.TryPop(out _);
            else
                stack.Push(c);

        return string.Concat(stack.Reverse().ToArray());
    }
}