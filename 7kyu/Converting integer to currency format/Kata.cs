using System.Text.RegularExpressions;

public class Kata
{
    public static string ToCurrency(int price)
    {
        // return string.Join(",", Regex.Split(price.ToString(), @"(?!^)(?=(?:\d{3})+$)"));
        return string.Join(",", Regex.Split(price.ToString(), @"(?=(?:\d{3})+$)(?!^)"));
        // return $"{price:N0}";
        // return price.ToString("N0");
    }
}