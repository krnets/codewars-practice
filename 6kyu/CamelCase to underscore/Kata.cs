using System.Text.RegularExpressions;

public static class CamelCaseTranslator
{
    public static string ToUnderScore(string name)
    {
        return Regex.Replace(name, @"([A-Za-z](?=[A-Z\d])|\d(?=[A-Z]))", @"$1_");
    }
}