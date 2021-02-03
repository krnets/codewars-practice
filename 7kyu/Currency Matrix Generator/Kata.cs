/*using System.Collections.Generic;
using System.Linq;

public class Kata
{
    public static string[] GenerateCurrencyMatrix(string currency)
    {
        var fx = new List<string> {"EUR", "GBP", "AUD", "NZD", "USD", "CAD", "CHF", "JPY"};
        var index = fx.IndexOf(currency);

        return fx.Where(c => c != currency)
            .Select(c => fx.IndexOf(c) < index ? c + currency : currency + c)
            .ToArray();
    }
}*/

using System.Collections.Generic;
using System.Linq;

public class Kata
{
    private static readonly List<string> Fx = new List<string>()
        {"EUR", "GBP", "AUD", "NZD", "USD", "CAD", "CHF", "JPY"};

    public static string[] GenerateCurrencyMatrix(string currency)
    {
        int index = Fx.IndexOf(currency);

        return Fx.Where(c => c != currency)
            .Select(c => Fx.IndexOf(c) < index ? c + currency : currency + c)
            .ToArray();
    }
}