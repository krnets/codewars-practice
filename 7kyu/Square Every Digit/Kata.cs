/*using System.Text;

public class Kata
{
    public static int SquareDigits(int n)
    {
        var nStr = n.ToString();
        var sb = new StringBuilder();

        foreach (var c in nStr)
        {
            int x = (int) char.GetNumericValue(c);
            sb.Append(x * x);
        }

        return int.Parse(sb.ToString());
    }
}*/

using System.Linq;

public class Kata
{
    public static int SquareDigits(int n)
    {
        string squared = n.ToString()
            .Select(char.GetNumericValue)
            .Select(x => x * x)
            .Aggregate("", (a, b) => a + b);

        return int.Parse(squared);
    }
}