public static class Kata
{
    public static long Fibonacci(int max)
    {
        long a = 0, b = 1;
        long sum = 0;

        while (b < max)
        {
            (a, b) = (b, a + b);
            sum += (a % 2 == 0 ? a : 0);
        }

        return sum;
    }
}