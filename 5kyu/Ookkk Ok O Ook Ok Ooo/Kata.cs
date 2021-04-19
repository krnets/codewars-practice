using System;
using System.Linq;

public class Kata
{
    public static string OkkOokOo(string okOokOoo)
    {
        return string.Concat(okOokOoo.ToLower()
            .Split("?")
            .Select(str =>
                (char) Convert.ToInt32(string.Concat(str.Select(c => c == 'o' ? "0" : c == 'k' ? "1" : "")), 2)));
    }
}