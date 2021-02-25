public class Kata
{
    public static string BandNameGenerator(string str)
    {
        var firstUpper = char.ToUpper(str[0]);

        return str[0] == str[^1] ? firstUpper + str[1..^1] + str : "The " + firstUpper + str[1..];
    }
}