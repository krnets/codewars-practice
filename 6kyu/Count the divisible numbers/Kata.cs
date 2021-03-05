public class Kata
{
    public static long DivisibleCount(long x, long y, long k)
    {
        return y / k - x / k + (x % k == 0 ? 1 : 0);
    }
}