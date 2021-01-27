/*public class DecTools
{
    public static int Digits(ulong n)
    {
        return n < 10 ? 1 : 1 + Digits(n / 10);
    }
}*/

/*public class DecTools
{
    public static int Digits(ulong n)
    {
        int count = 1;

        while (n > 10l)
        {
            n /= 10l;
            count++;
        }

        return count;
    }
}*/

public class DecTools
{
    public static int Digits(ulong n)
    {
        return n.ToString().Length;
    }
}