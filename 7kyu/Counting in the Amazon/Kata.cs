using System.Linq;
using static System.Linq.Enumerable;

public class Kata
{
    public static string CountArara(int n)
    {
        return string.Join(' ', Repeat("adak", n / 2).Concat(Repeat("anane", n % 2)));
    }
}