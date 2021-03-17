using System.Linq;
using System.Text;

class MissingAlphabet
{
    public static string InsertMissingLetters(string str)
    {
        var sb = new StringBuilder();
        var alphabet = Enumerable.Range('a', 26).Select(i => (char) i).ToList();
        var charSet = str.ToHashSet();

        foreach (char c in str)
        {
            if (charSet.Contains(c))
            {
                sb.Append(c).Append(string.Concat(alphabet.Skip(alphabet.IndexOf(c)).Except(str)).ToUpper());
                charSet.Remove(c);
            }
            else sb.Append(c);
        }

        return sb.ToString();
    }
}