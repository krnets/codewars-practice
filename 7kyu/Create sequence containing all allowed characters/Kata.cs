/*using System.Text;
using System.Text.RegularExpressions;

public class Kata
{
    public string CreateSequence(Regex regex)
    {
        var sb = new StringBuilder();

        for (char c = '0'; c <= 'z'; c++)
            if (regex.IsMatch(char.ToString(c)))
                sb.Append(c);

        return sb.ToString();
    }
}*/

using System.Linq;
using System.Text.RegularExpressions;

public class Kata
{
    public string CreateSequence(Regex regex)
    {
        return string.Concat(
            Enumerable.Range(0, 128)
                .Select(i => (char) i)
                .Where(c => regex.IsMatch(char.ToString(c))));
    }
}