class Kata
{
    private static string[] First20 =
    {
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven",
        "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"
    };

    private static string[] Tens =
        {"ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"};

    public static string NumberToEnglish(int n)
    {
        if (n < 0) return string.Empty;

        if (n < 20) return First20[n];

        if (n < 100)
            return $"{Tens[n / 10 - 1]}{(n % 10 > 0 ? $" {First20[n % 10]}" : "")}";

        if (n < 1000)
            return $"{First20[n / 100]} hundred{(n % 100 > 0 ? $" {NumberToEnglish(n % 100)}" : "")}";

        return $"{NumberToEnglish(n / 1000)} thousand{(n % 1000 > 0 ? $" {NumberToEnglish(n % 1000)}" : "")}";
    }
}