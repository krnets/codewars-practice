/*using System.Linq;

public class Kata
{
    public static string[] WordSearch(string query, string[] seq)
    {
        var queryLower = query.ToLower();
        var result = seq.Where(w => w.ToLower().Contains(queryLower)).ToArray();

        return result.Length == 0 ? new[] { "Empty" } : result;
    }
}*/

using System.Linq;

public class Kata
{
    public static string[] WordSearch(string query, string[] seq)
    {
        var queryLower = query.ToLower();

        return seq.Where(w => w.ToLower().Contains(queryLower)).DefaultIfEmpty("Empty").ToArray();
    }
}