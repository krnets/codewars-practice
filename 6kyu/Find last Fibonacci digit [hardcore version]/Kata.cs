/*using System.Linq;
using System.Text;

public class Kata
{
    public static int LastFibDigit(long n)
    {
        int a = 0, b = 1;
        var sb = new StringBuilder();

        while (sb.Length < 60)
        {
            sb.Append(a);
            (a, b) = (b, (a + b) % 10);
        }

        return sb.ToString().Take(60).ElementAt((int) (n % 60)) - '0';
    }
}*/

public class Kata
{
    public static int LastFibDigit(long n)
    {
        var arr = new int[60];
        arr[1] = 1;

        for (int i = 2; i < 60; i++)
            arr[i] = (arr[i - 2] + arr[i - 1]) % 10;

        return arr[n % 60];
    }
}