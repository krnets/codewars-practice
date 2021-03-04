/*using System.Text;
using static System.String;

public class Kata
{
    public static string Palindromization(string elements, int n)
    {
        if (IsNullOrEmpty(elements) || elements.Length < 2 || n < 2) return "Error!";

        var front = new StringBuilder();
        var back = new StringBuilder();
        string mid = default;

        for (int i = 0; i <= n / 2; i++)
        {
            var c = elements[i % elements.Length];

            if (i == n / 2)
                mid = char.ToString(c);
            else
            {
                front.Append(c);
                back.Insert(0, c);
            }
        }

        return $"{front}{(n % 2 == 0 ? Empty : mid)}{back}";
    }
}*/

using System.Linq;
using System.Text;
using static System.String;

public class Kata
{
    public static string Palindromization(string elements, int n)
    {
        if (IsNullOrEmpty(elements) || elements.Length < 2 || n < 2) return "Error!";

        var sb = new StringBuilder();

        for (int i = 0; i < n / 2; i++)
            sb.Append(elements[i % elements.Length]);

        return $"{sb}{(n % 2 == 0 ? Empty : $"{elements[n / 2 % elements.Length]}")}{Concat($"{sb}".Reverse())}";
    }
}