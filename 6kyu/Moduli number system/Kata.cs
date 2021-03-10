using System.Linq;

public class ModSystem
{
    public static string fromNb2Str(int n, int[] sys)
    {
        return n < sys.Aggregate((p, m) => p * m) && sys.Count(i => i % 2 == 0) < 2
            // ? $"-{string.Join("--", sys.Select(i => $"{n % i}"))}-"
            ? string.Concat(sys.Select(i => $"-{n % i}-"))
            : "Not applicable";
    }
}