/*using System.Text.RegularExpressions;

public class Kata
{
    public static string ReplaceAll(string input, string find, string replace)
    {
        return Regex.Replace(input, Regex.Escape(find), replace);
    }
}*/

using System.Linq;

public class Kata
{
    public static string ReplaceAll(string input, string find, string replace)
    {
        if (string.IsNullOrEmpty(find))
            return replace + string.Concat(input.Select(c => c + replace));

        for (int i = 0, nextIndex; i < input.Length;)
        {
            nextIndex = input.IndexOf(find, i);

            input = nextIndex < 0 ? input : input[..nextIndex] + replace + input[(nextIndex + find.Length)..];

            i += nextIndex < 0 ? 1 : replace.Length;
        }

        return input;
    }
}