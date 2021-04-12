public class NumberTranslation
{
    private static readonly string[] First20 =
    {
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven",
        "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"
    };

    private static readonly string[] Tens =
        {"ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"};

    public static string Number2Words(int n)
    {
        if (n < 20) return First20[n];
        if (n < 100) return $"{Tens[n / 10 - 1]}{(n % 10 > 0 ? $"-{First20[n % 10]}" : "")}";
        if (n < 1000) return $"{First20[n / 100]} hundred{(n % 100 > 0 ? $" {Number2Words(n % 100)}" : "")}";

        return $"{Number2Words(n / 1000)} thousand{(n % 1000 > 0 ? $" {Number2Words(n % 1000)}" : "")}";
    }
}