using System.Linq;

public class Hamming
{
    public static int Distance(string a, string b)
    {
        return a.Zip(b, (f, s) => f != s).Count(x => x);
        // return a.Where((c, i) => c != b[i]).Count();
    }
}