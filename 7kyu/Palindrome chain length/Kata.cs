public static class Kata
{
    public static int palindromeChainLength(int n)
    {
        int steps = 0;
        long num = n;
        long numReversed = ReverseNumber(num);

        while (num != numReversed)
        {
            num += numReversed;
            numReversed = ReverseNumber(num);
            steps++;
        }

        return steps;
    }

    private static long ReverseNumber(long num)
    {
        long result = 0, remainder;

        while (num != 0)
        {
            remainder = num % 10;
            result = result * 10 + remainder;
            num /= 10;
        }

        return result;
    }
}