using System.Linq;

namespace Solution
{
    public static class Program
    {
        public static string alternateCase(string s)
        {
            return string.Concat(s.Select(c => char.IsUpper(c) ? char.ToLower(c) : char.ToUpper(c)));
        }
    }
}