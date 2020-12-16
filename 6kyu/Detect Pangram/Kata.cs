using System.Linq;

public static class Kata
{
    public static bool IsPangram(string str)
    {
        return str.ToLower().Distinct().Where(char.IsLetter).Count() == 26;
    }
}