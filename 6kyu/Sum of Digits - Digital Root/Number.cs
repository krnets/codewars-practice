/*public class Number
{
    public int DigitalRoot(long n)
    {
        if (n < 10) return (int) n;

        long sum = 0;

        while (n > 0)
        {
            sum += n % 10;
            n /= 10;
        }

        return DigitalRoot(sum);
    }
}*/

using System;
using System.Linq;

public class Number
{
    public int DigitalRoot(long n)
    {
        while (n > 9)
            n = n.ToString().Select(c => Convert.ToInt32(c.ToString())).Sum();

        return (int) n;
    }
}

/*
public class Number
{
    public int DigitalRoot(long n)
    {
        return (int) (1 + (n - 1) % 9);
    }
}
*/