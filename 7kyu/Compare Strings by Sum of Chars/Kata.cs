using System.Linq;

public static class Kata
{
    public static bool Compare(string s1, string s2)
    {
        return SumOfChars(s1 ?? "") == SumOfChars(s2 ?? "");
    }

    private static int SumOfChars(string s)
    {
        return s.All(char.IsLetter) ? s.ToUpper().Sum(c => c) : 0;
    }
}