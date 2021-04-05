/*using System.Linq;

public class Kata
{
    public static string GetStrings(string city)
    {
        var map = city.ToLower().GroupBy(c => c).ToDictionary(g => g.Key, g => g.Count());

        return string.Join(",", city.ToLower().Distinct().Where(char.IsLetter).Select(c => $"{c}:{new string('*', map[c])}"));
    }
}*/

using System.Linq;

public class Kata
{
    public static string GetStrings(string city)
    {
        return string.Join(",",
            city
                .Where(char.IsLetter)
                .GroupBy(char.ToLower)
                .Select(g => $"{g.Key}:{new string('*', g.Count())}"));
    }
}