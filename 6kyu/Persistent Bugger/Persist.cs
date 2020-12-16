using System.Linq;

public class Persist
{
    public static int Persistence(long n)
    {
        int count = 0;

        while (n > 9)
        {
            // n = n.ToString().Select(c => Convert.ToInt32(c.ToString())).Aggregate((a, b) => a * b);
            // n = n.ToString().Select(char.GetNumericValue).Aggregate(1, (a, b) => a * (int) b);
            n = n.ToString().Aggregate(1, (a, b) => a * (b - '0'));
            count++;
        }

        return count;
    }
}

/*public class Persist
{
    public static int Persistence(long n)
    {
        int count = 0;

        while (n > 9)
        {
            long mul = 1;
            while (n > 0)
            {
                mul *= n % 10;
                n /= 10;
            }

            n = mul;
            count++;
        }

        return count;
    }
}*/