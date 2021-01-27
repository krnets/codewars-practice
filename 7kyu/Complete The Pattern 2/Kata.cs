/*public class Kata
{
    public string Pattern(int n)
    {
        string row = "", output = "";

        while (n > 0)
            output = (row += n--) + "\n" + output;

        return output.TrimEnd();
    }
}*/

using System.Linq;
using static System.Linq.Enumerable;
using static System.Math;
using static System.String;

public class Kata
{
    public string Pattern(int n)
    {
        return Join('\n', Range(0, Max(n, 0))
            .Select(i => Concat(Range(0, n - i)
                .Select(j => n - j))));
    }
}