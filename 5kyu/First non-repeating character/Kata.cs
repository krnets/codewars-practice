/*public class Kata
{
    public static string FirstNonRepeatingLetter(string s)
    {
        var upper = s.ToUpper();

        for (int i = 0; i < upper.Length; i++)
            if (upper.IndexOf(upper[i]) == upper.LastIndexOf(upper[i]))
                return s[i].ToString();

        return string.Empty;
    }
}*/

using System.Linq;

public class Kata
{
    public static string FirstNonRepeatingLetter(string s)
    {
        var firstUnique = s.ToUpper()
            .GroupBy(c => c)
            .ToDictionary(g => g.Key, g => g.Count())
            .FirstOrDefault(p => p.Value == 1).Key;

        return firstUnique == default ? string.Empty : s.First(c => char.ToUpper(c) == firstUnique).ToString();
    }
}