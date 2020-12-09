/*using System.Linq;

public static class JadenCase
{
    public static string ToJadenCase(this string phrase)
    {
        return string.Join(' ', phrase.Split(' ').Select(word => char.ToUpper(word[0]) + word.Substring(1)));
    }
}*/

using static System.Globalization.CultureInfo;

public static class JadenCase
{
    public static string ToJadenCase(this string phrase)
    {
        return CurrentCulture.TextInfo.ToTitleCase(phrase);
    }
}