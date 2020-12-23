using System.Text;

public class Kata
{
    public static string Encrypt(string text, int n)
    {
        if (n <= 0 || text == null) return text;

        var even = new StringBuilder();
        var odd = new StringBuilder();

        for (int i = 0; i < text.Length; i++)
            if (i % 2 == 0)
                even.Append(text[i]);
            else odd.Append(text[i]);

        return Encrypt(odd.Append(even).ToString(), n - 1);
    }

    public static string Decrypt(string encryptedText, int n)
    {
        if (n <= 0 || encryptedText == null) return encryptedText;

        var sb = new StringBuilder();
        int mid = encryptedText.Length / 2;

        for (int i = 0; i < mid; i++)
            sb.Append(encryptedText[mid + i])
                .Append(encryptedText[i]);

        if (encryptedText.Length % 2 == 1)
            sb.Append(encryptedText[^1]);

        return Decrypt(sb.ToString(), n - 1);
    }
}