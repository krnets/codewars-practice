/*using System.Text.RegularExpressions;

public static class Kata
{
    public static string getIssuer(long number)
    {
        var card = number.ToString();
        
        var amex = @"^3[47]\d{13}$";
        var discover = @"^6011\d{12}$";
        var mastercard = @"^5[1-5]\d{14}$";
        var visa = @"^4(\d{12}|\d{15})$";

        if (Regex.IsMatch(card, amex))
            return "AMEX";

        if (Regex.IsMatch(card, discover))
            return "Discover";

        if (Regex.IsMatch(card, mastercard))
            return "Mastercard";

        return Regex.IsMatch(card, visa) ? "VISA" : "Unknown";
    }
}*/

using System.Collections.Generic;
using System.Text.RegularExpressions;

public static class Kata
{
    private static readonly Dictionary<string, string> Issuer = new Dictionary<string, string>()
    {
        {"AMEX", @"^3[47]\d{13}$"},
        {"Discover", @"^6011\d{12}$"},
        {"Mastercard", @"^5[1-5]\d{14}$"},
        {"VISA", @"^4(\d{12}|\d{15})$"}
    };

    public static string getIssuer(long number)
    {
        var card = number.ToString();

        foreach (var (key, value) in Issuer)
            if (Regex.IsMatch(card, value))
                return key;

        return "Unknown";
    }
}