public static class Kata
{
    private static int[] holes = new int[] {1, 0, 0, 0, 0, 0, 1, 0, 2, 1};

    public static int GetNum(long n)
    {
        return n == 0 ? 0 : holes[n % 10] + GetNum(n / 10);
    }
}