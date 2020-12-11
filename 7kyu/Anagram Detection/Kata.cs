using System.Linq;

public class Kata
{
    public static bool IsAnagram(string test, string original)
    {
        static string SortCharsInString(string s) => string.Concat(s.ToLower().OrderBy(c => c));

        var a = SortCharsInString(test);
        var b = SortCharsInString(original);

        return a.Equals(b);
    }
}