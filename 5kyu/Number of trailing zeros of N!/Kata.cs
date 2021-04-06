public static class Kata
{
    public static int TrailingZeros(int n)
    {
        return n < 5 ? 0 : n / 5 + TrailingZeros(n / 5);
    }
}