using System;
using System.Linq;

namespace AsciiResort
{
    public static class Slope
    {
        public static string DetermineCool(int incline, string name)
        {
            return Convert.ToString(name.Sum(c => c), incline);
        }
    }
}