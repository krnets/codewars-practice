/*using System.Linq;
using System.Text.RegularExpressions;

public class Kata
{
    public static bool isAValidMessage(string message)
    {
        if (message.Length == 0) return true;

        var array = Regex.Matches(message, @"\d+|[A-Za-z]+").Select(m => m.Value).ToArray();

        if (array.Length % 2 != 0) return false;

        for (int i = 0; i < array.Length - 1; i += 2)
        {
            var parseResult = int.TryParse(array[i], out int len);

            if (!parseResult || len != array[i + 1].Length)
                return false;
        }

        return true;
    }
}*/

/*using System.Linq;
using System.Text.RegularExpressions;

public class Kata
{
    public static bool isAValidMessage(string message)
    {
        return message == string.Empty || char.IsDigit(message[0]) && char.IsLetter(message[^1]) &&
            Regex.Matches(message, @"(\d+)([A-Za-z]+)")
                .All(m => int.Parse(m.Groups[1].Value) == m.Groups[2].Value.Length);
    }
}*/

using System.Linq;
using System.Text.RegularExpressions;

public class Kata
{
    public static bool isAValidMessage(string message)
    {
        return Regex.Matches(message, @"(?<num>\d+)(?<word>[A-Za-z]+)?")
            .All(m => int.TryParse(m.Groups["num"].Value, out int length) && (m.Groups["word"].Value.Length == length));
    }
}