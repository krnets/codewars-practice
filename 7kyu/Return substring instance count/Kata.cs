//using System.Linq;
using System.Text.RegularExpressions;

public class Kata
{
    public static int SubstringCount(string fullText, string searchText)
    {
        // return Regex.Matches(fullText, searchText).Count();
        return Regex.Matches(fullText, searchText).Count;
        // return new Regex(searchText).Matches(fullText).Count;
    }
}