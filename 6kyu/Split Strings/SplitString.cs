/*using System.Collections.Generic;

public class SplitString
{
    public static string[] Solution(string str)
    {
        var list = new List<string>();
        str += '_';

        for (int i = 0; i < str.Length - 1; i += 2)
            list.Add(str[i..(i + 2)]);

        return list.ToArray();
    }
}*/

using System.Linq;
using System.Text.RegularExpressions;

public class SplitString
{
    public static string[] Solution(string str)
    {
        return Regex.Matches(str + '_', "..").Select(m => m.Value).ToArray();
    }
}

/*public class SplitString
{
    public static string[] Solution(string str)
    {
        if (str.Length % 2 == 1)
            str += "_";

        string[] result = new string[str.Length / 2];

        for (int i = 0; i < str.Length; i += 2)
            result[i / 2] = str[i..(i + 2)];

        return result;
    }
}*/