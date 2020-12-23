using System;
using System.Linq;
using System.Globalization;

/*
namespace Kata
{
    public static class Problem
    {
        public static string CamelCase(this string str)
        {
            var ti = CultureInfo.CurrentCulture.TextInfo;

            return string.Concat(str.Split().Select(w => ti.ToTitleCase(w)));
        }
    }
}*/

/*namespace Kata
{
    public static class Problem
    {
        public static string CamelCase(this string str)
        {
            return CultureInfo.CurrentCulture.TextInfo.ToTitleCase(str).Replace(" ", string.Empty);
        }
    }
}*/

namespace Kata
{
    public static class Problem
    {
        public static string CamelCase(this string str)
        {
            return string.Concat(str.Split().Select(TitleCase));
        }

        private static string TitleCase(string word)
        {
            return word.Length > 0 ? char.ToUpper(word[0]) + word[1..].ToLower() : word;
        }
    }
}