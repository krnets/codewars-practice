/*using System.Linq;

public class Kata
{
    public static string Spam(int n)
    {
        const string SpamValue = "hue";

        return string.Concat(Enumerable.Repeat(SpamValue, n));
    }
}*/

using System.Text;

public class Kata
{
    public static string Spam(int n)
    {
        const string SpamValue = "hue";

        return new StringBuilder().Insert(0, SpamValue, n).ToString();
    }
}