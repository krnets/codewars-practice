using System.Linq;

namespace Solution
{
/*using System;

{
    class Kata
    {
        public static int binaryArrayToNumber(int[] BinaryArray)
        {
            string joined = String.Join("", BinaryArray);

            return Convert.ToInt32(joined, 2);
        }
    }
}*/
    class Kata
    {
        public static int binaryArrayToNumber(int[] BinaryArray)
        {
            // return BinaryArray.Aggregate(0, (sum, el) => 2 * (sum + el)) / 2;
            // return BinaryArray.Aggregate((acc, bit) => (acc << 1) | bit);
            return BinaryArray.Aggregate((acc, bit) => (2 * acc) | bit);
        }
    }
}