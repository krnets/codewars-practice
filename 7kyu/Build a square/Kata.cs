/*using System.Linq;
using static System.Linq.Enumerable;
using static System.String;

public static class Kata
{
    public static string GenerateShape(int n)
    {
        return Join('\n', Range(0, n).Select(_ => Concat(Repeat('+', n))));
    }
}*/

using static System.Linq.Enumerable;
using static System.String;

public static class Kata
{
    public static string GenerateShape(int n)
    {
        return Join('\n', Repeat(new string('+', n), n));
    }
}