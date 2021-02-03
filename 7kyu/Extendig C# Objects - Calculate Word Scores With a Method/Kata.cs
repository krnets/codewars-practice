using System.Linq;

namespace CustomExtensions
{
    public static class MyExtensionMethods
    {
        public static int Score(this string str)
        {
            return str.ToLower().Where(char.IsLetter).Sum(c => c - 'a' + 1);
        }
    }
}