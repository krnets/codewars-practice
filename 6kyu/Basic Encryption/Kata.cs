using System.Linq;

public static class Kata
{
    public static string Encrypt(string text, int rule)
    {
        return string.Concat(text.Select(c => (char) ((c + rule) % 256)));
    }
}

/*using System.Linq;

public static class Kata
{
    public static string Encrypt(string text, int rule)
    {
        return text.Aggregate("", (acc, c) => acc + (char) ((c + rule) % 256));
    }
}*/