/*using System.Linq;

class Solution
{
    public static int Stray(int[] numbers)
    {
        return numbers.Aggregate((a, b) => a ^ b);
    }
}*/

using System;
using System.Linq;

class Solution
{
    public static int Stray(int[] numbers)
    {
        Array.Sort(numbers);
        return numbers[0] == numbers[1] ? numbers.Last() : numbers.First();
    }
}