using System.Collections.Generic;

public class Kata
{
    private static Dictionary<int, int> fCache = new Dictionary<int, int>();
    private static Dictionary<int, int> mCache = new Dictionary<int, int>();

    public static int F(int n)
    {
        if (n == 0) return 1;

        if (!fCache.ContainsKey(n))
            fCache[n] = n - M((F(n - 1)));

        return fCache[n];
    }

    public static int M(int n)
    {
        if (n == 0) return 0;

        if (!mCache.ContainsKey(n))
            mCache[n] = n - F(M(n - 1));

        return mCache[n];
    }
}