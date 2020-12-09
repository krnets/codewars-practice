using System.Linq;

public static class Kata
{
    public static string Solution(string str)
    {
        // return Microsoft.VisualBasic.Strings.StrReverse(str);
        // return new string(str.Reverse().ToArray());
        return string.Concat(str.Reverse());
    }
}