/*public class Sequence 
{
    public static long GetScore(long n) 
    {
        return 25 * n * (n + 1);
    }
}*/

public class Sequence
{
    public static long GetScore(long n)
    {
        return 50 * (n * (n + 1) / 2);
    }
}

/*public class Sequence
{
    public static long GetScore(long n)
    {
        long acc = 0;

        for (long i = 0; i < n; i++)
            acc += 50 * i;

        return acc + 50 * n;
    }
}*/

/*public class Sequence
{
    public static long GetScore(long n)
    {
        return n == 1 ? 50 : 50 * n + GetScore(n - 1);
    }
}*/