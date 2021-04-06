using System.Linq;

public class Scramblies
{
    public static bool Scramble(string str1, string str2)
    {
        var str1CharCount = str1.GroupBy(c => c)
            .ToDictionary(g => g.Key, g => g.Count());

        foreach (char c in str2)
            if (str1CharCount.ContainsKey(c))
                str1CharCount[c]--;
            else return false;

        return str1CharCount.Values.All(x => x >= 0);
    }
}

/*using System.Linq;

public class Scramblies
{
    public static bool Scramble(string str1, string str2)
    {
        var str1CharCount = str1.GroupBy(c => c)
            .ToDictionary(g => g.Key, g => g.Count());

        foreach (char c in str2)
        {
            if (str1CharCount.ContainsKey(c))
            {
                if (str1CharCount[c] == 0)
                    return false;
                str1CharCount[c]--;
            }
            else return false;
        }

        return true;
    }
}*/