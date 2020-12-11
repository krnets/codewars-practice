/*using System;

public class Kata
{
    public static int SumDigits(int number)
    {
        int sum = 0;
        number = Math.Abs(number);

        while (number > 0)
        {
            sum += number % 10;
            number /= 10;
        }

        return sum;
    }
}*/

using System.Linq;

public class Kata
{
    public static int SumDigits(int number)
    {
        return number.ToString().Trim('-').Select(c => int.Parse(c.ToString())).Sum();
    }
}