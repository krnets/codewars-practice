/*using System;
using System.Linq;

namespace BinaryOperators
{
    public class BitCounting
    {
        public static bool SharedBits(int a, int b)
        {
            return Convert.ToString(a & b, 2).Count(x => x == '1') >= 2;
        }
    }
}*/

using System.Numerics;

namespace BinaryOperators
{
    public class BitCounting
    {
        public static bool SharedBits(int a, int b) => BitOperations.PopCount((uint) (a & b)) >= 2;
    }
}