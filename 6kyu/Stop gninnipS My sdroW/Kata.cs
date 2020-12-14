using System.Linq;

public class Kata
{
    public static string SpinWords(string sentence)
    {
        return string.Join(' ', sentence.Split(' ').Select(w => w.Length < 5 ? w : string.Concat(w.Reverse())));
    }
}

/*using System.Linq;
using System.Text.RegularExpressions;

public class Kata
{
    public static string SpinWords(string sentence)
    {
        return Regex.Replace(sentence, @"\w{5,}", m => string.Concat(m.Value.Reverse()));
    }
}*/