/*using System.Collections.Generic;
using System.Globalization;
using System.Text.RegularExpressions;

public class Kata
{
    public static string ToCamelCase(string str)
    {
        var array = Regex.Split(str, "[_-]");
        var list = new List<string> {array[0]};
        var ti = CultureInfo.CurrentCulture.TextInfo;

        for (int i = 1; i < array.Length; i++)
            list.Add(ti.ToTitleCase(array[i]));

        return string.Concat(list);
    }
}*/

using System.Text.RegularExpressions;

public class Kata
{
    public static string ToCamelCase(string str)
    {
        return Regex.Replace(str, @"[_-](\w)", m => m.Groups[1].Value.ToUpper());
    }
}