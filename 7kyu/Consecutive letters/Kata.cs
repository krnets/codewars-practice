/*using System.Linq;

public class Solution
{
    public static bool solve(string s)
    {
        var arr = s.OrderBy(c => c).ToArray();

        return arr.Length == arr.Distinct().Count() && arr.Select((c, i) => c - i == arr[0]).All(x => x);
    }
}*/

using System.Linq;

public class Solution
{
    public static bool solve(string s)
    {
        var arr = s.OrderBy(c => c).ToArray();

        return Enumerable.Range(1, arr.Length - 1).All(i => arr[i] - arr[i - 1] == 1);
    }
}