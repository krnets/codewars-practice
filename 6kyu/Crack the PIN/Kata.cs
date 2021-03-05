using System;
using System.Security.Cryptography;
using System.Text;

public class CodeWars
{
    public static string crack(string hash)
    {
        var md5 = MD5.Create();
        var encoding = new UTF8Encoding();
        var expectedHash = hash.ToUpper();

        for (int pin = 0; pin < 100_000; pin++)
        {
            var pinStr = $"{pin:D5}";
            var calcHash = BitConverter.ToString(
                    md5.ComputeHash(
                        encoding.GetBytes(pinStr)))
                .Replace("-", string.Empty);

            if (calcHash == expectedHash)
                return pinStr;
        }

        return string.Empty;
    }
}