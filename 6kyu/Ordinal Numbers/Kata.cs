public class Kata
{
    public static string Ordinal(int number, bool brief = false)
    {
        var ordB = new[] {"th", "st", "d", "d"};
        var ordG = new[] {"th", "st", "nd", "rd"};
        var suffix = "th";

        if ((number % 100 < 4 || number % 100 > 13) && (number % 10 < 4))
            suffix = (brief ? ordB : ordG)[number % 10];

        return suffix;
    }
}