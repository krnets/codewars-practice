public class ProdFib
{
    public static ulong[] productFib(ulong prod)
    {
        ulong a = 0, b = 1;

        while (a * b < prod)
            (a, b) = (b, a + b);

        return new[] {a, b, (ulong) (a * b == prod ? 1 : 0)};
        // return new[] {a, b, (a * b == prod ? 1UL : 0UL)};
    }
}