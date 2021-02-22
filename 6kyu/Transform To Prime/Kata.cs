using System;
using System.Linq;

namespace TransformToPrime
{
    class Solution
    {
        public static int MinimumNumber(int[] numbers)
        {
            var sum = numbers.Sum();
            int x = (sum + 1) % 2;

            while (!IsPrime(sum + x))
                x += 2;

            return x;
        }

        private static bool IsPrime(int num)
        {
            if (num <= 1) return false;
            if (num <= 3) return true;
            if (num % 2 == 0 || num % 3 == 0) return false;

            for (int i = 5; i <= Math.Sqrt(num); i += 6)
                if (num % i == 0 || num % (i + 2) == 0)
                    return false;

            return true;
        }
    }
}