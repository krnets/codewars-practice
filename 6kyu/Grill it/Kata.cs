/*
using System;
using System.Linq;

public class Kata
{
    public static string Grille(string message, int code)
    {
        var bits = Convert.ToString(code, 2).PadLeft(message.Length, '0');

        if (bits.Length > message.Length)
            message = message.PadLeft(bits.Length, ' ');

        return string.Concat(bits.Zip(message, (bit, c) => bit == '1' ? $"{c}" : "")).Trim();
    }
}
*/

/*using System;
using System.Text;

public class Kata
{
    public static string Grille(string message, int code)
    {
        var bits = Convert.ToString(code, 2).PadLeft(message.Length, '0');
        var sb = new StringBuilder();

        for (int i = 0; i < message.Length; i++)
            if (bits[i] == '1')
                sb.Append(message[i]);

        return sb.ToString().Trim();
    }
}*/

/*using System.Linq;
using System.Text;

public class Kata
{
    public static string Grille(string message, int code)
    {
        var sb = new StringBuilder();

        foreach (char c in message.Reverse())
        {
            if ((code & 1) == 1)
                sb.Insert(0, c);

            code >>= 1;
        }

        return sb.ToString();
    }
}*/

using System.Linq;

public class Kata
{
    public static string Grille(string message, int code)
    {
        return string.Concat(message.Where((_, i) => (code & 1 << message.Length - i - 1) != 0));
    }
}