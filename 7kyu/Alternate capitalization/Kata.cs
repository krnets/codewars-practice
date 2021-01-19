/*using System.Text;

public static class Kata
{
    public static string[] Capitalize(string s)
    {
        var sbEven = new StringBuilder();
        var sbOdd = new StringBuilder();

        for (int i = 0; i < s.Length; i++)
        {
            if (i % 2 == 0)
            {
                sbEven.Append(char.ToUpper(s[i]));
                sbOdd.Append(s[i]);
            }
            else
            {
                sbEven.Append(s[i]);
                sbOdd.Append(char.ToUpper(s[i]));
            }
        }

        return new string[] { sbEven.ToString(), sbOdd.ToString() };
    }
}*/

/*using System.Text;

public static class Kata
{
    public static string[] Capitalize(string s)
    {
        var sbEven = new StringBuilder(s);
        var sbOdd = new StringBuilder(s);

        for (int i = 0; i < s.Length; i++)
        {
            if (i % 2 == 0)
                sbEven[i] = char.ToUpper(sbEven[i]);
            else
                sbOdd[i] = char.ToUpper(sbOdd[i]);
        }

        return new string[] { sbEven.ToString(), sbOdd.ToString() };
    }
}
*/

using System.Linq;

public static class Kata
{
    public static string[] Capitalize(string s)
    {
        return Enumerable.Range(0, 2)
                         .Select(h => string.Concat(s.Select((c, i) => i % 2 == h ? char.ToUpper(c) : c)))
                         .ToArray();
    }
}