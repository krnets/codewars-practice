public static class Kata
{
    private static int Gcd(int x, int y) => x % y == 0 ? y : Gcd(y, x % y);

    public static bool Solve(int a, int b)
    {
        var c = Gcd(a, b);

        while (c > 1)
        {
            b /= c;
            c = Gcd(a, b);
        }

        return b == 1;
    }
}