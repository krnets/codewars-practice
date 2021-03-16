/*using System.Text;

class Kata
{
    public static string NumericFormatter(string template, string digits = "1234567890")
    {
        var sb = new StringBuilder();
        int i = 0;

        foreach (char c in template)
        {
            if (char.IsLetter(c))
            {
                sb.Append(digits[i % digits.Length]);
                i++;
            }
            else sb.Append(c);
        }

        return sb.ToString();
    }
}*/

using System.Text.RegularExpressions;

class Kata
{
    public static string NumericFormatter(string template, string digits = "1234567890")
    {
        int index = 0;

        return Regex.Replace(template, "[A-z]", _ => digits[index++ % digits.Length].ToString());
    }
}