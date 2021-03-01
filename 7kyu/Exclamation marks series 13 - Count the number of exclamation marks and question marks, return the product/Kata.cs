public class Kata
{
    public static int Product(string str)
    {
        var exclamationMarkCount = 0;
        var questionMarkCount = 0;

        foreach (char c in str)
        {
            if (c == '!') exclamationMarkCount++;
            else if (c == '?') questionMarkCount++;
        }

        return exclamationMarkCount * questionMarkCount;
    }
}