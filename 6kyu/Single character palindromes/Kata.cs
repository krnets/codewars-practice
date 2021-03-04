/*using System.Linq;
using System.Text;

public class Solution
{
    private static bool IsPalindrome(string s) => s.Reverse().SequenceEqual(s);

    public static string solve(string s)
    {
        return IsPalindrome(s) ? "OK" :
            s.Select((_, i) => new StringBuilder(s).Remove(i, 1).ToString()).Any(IsPalindrome) ? "remove one" :
            "not possible";
    }
}*/

using System.Linq;

public class Solution
{
    private static bool IsPalindrome(string s) => s.Reverse().SequenceEqual(s);

    public static string solve(string s)
    {
        return IsPalindrome(s) ? "OK" :
            s.Select((_, i) => s.Remove(i, 1)).Any(IsPalindrome) ? "remove one" :
            "not possible";
    }
}