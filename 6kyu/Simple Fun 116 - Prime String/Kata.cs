/*public class Kata
{
    public bool PrimeString(string s)
    {
        return (s + s).IndexOf(s, 1) == s.Length;
    }
}*/

using System.Text.RegularExpressions;

public class Kata
{
    public bool PrimeString(string s)
    {
        return !Regex.IsMatch(s, @"^(.+)\1+$");
    }
}