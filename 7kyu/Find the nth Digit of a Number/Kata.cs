/*using System;

public class Kata
{
    public static int FindDigit(int num, int nth)
    {
        if (nth < 1) return -1;

        int result = 0;

        while (nth > 0)
        {
            nth--;

            if (nth == 0)
                result = num % 10;

            num /= 10;
        }

        return Math.Abs(result);
    }
}*/

using System;

public class Kata
{
    public static int FindDigit(int num, int nth)
    {
        return nth < 1 ? -1 : (int) (Math.Abs(num / Math.Pow(10, nth - 1)) % 10);
    }
}