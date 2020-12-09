using System.Linq;

public static class Kata
{
    /*
    public static string HighAndLow(string numbers)
    {
        var list = numbers.Split(" ").Select(int.Parse).ToList();

        return $"{list.Max()} {list.Min()}";
    }
*/
    public static string HighAndLow(string numbers)
    {
        var parsed = numbers.Split().Select(int.Parse);

        return parsed.Max() + " " + parsed.Min();
    }
}