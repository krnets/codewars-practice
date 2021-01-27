using System.Linq;

public class Kata
{
    public static string[][] search_names(string[][] logins)
    {
        return logins.Where(member => member[0].EndsWith('_')).ToArray();
    }
}