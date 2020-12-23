/*using System.Collections.Generic;

public class Kata
{
    public static string BreakCamelCase(string str)
    {
        var list = new List<string>();

        for (int i = 0, start = 0; i < str.Length; i++)
        {
            if (char.IsUpper(str[i]))
            {
                list.Add(str[start..i]);
                start = i;
            }

            if (i == str.Length - 1)
                list.Add(str[start..]);
        }

        return string.Join(" ", list);
    }
}*/

using System.Text.RegularExpressions;

public class Kata
{
    public static string BreakCamelCase(string str)
    {
        // return new Regex("([A-Z])").Replace(str, " $1");
        return Regex.Replace(str, "([A-Z])", match => $" {match.Value}");
    }
}