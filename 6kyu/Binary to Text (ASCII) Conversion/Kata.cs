/*using System;
using System.Text;

public static class Kata
{
    public static string BinaryToString(string binary)
    {
        var text = new StringBuilder();

        for (int i = 0; i < binary.Length; i += 8)
        {
            var c = (char) Convert.ToInt32(binary[i..(i + 8)], 2);
            text.Append(c);
        }

        return text.ToString();
    }
}*/

/*using System;
using System.Linq;
using System.Text.RegularExpressions;

public static class Kata
{
    public static string BinaryToString(string binary)
    {
        return string.Concat(Regex.Matches(binary, ".{8}").Select(m => (char) Convert.ToInt32(m.Value, 2)));
    }
}*/

using System;
using System.Text;

public static class Kata
{
    public static string BinaryToString(string binary)
    {
        const int bits = 8;
        var bytes = new byte[binary.Length / bits];

        for (int i = 0; i < bytes.Length; i++)
        {
            int bitIndex = bits * i;
            bytes[i] = Convert.ToByte(binary[bitIndex..(bitIndex + bits)], 2);
        }

        return Encoding.ASCII.GetString(bytes);
    }
}