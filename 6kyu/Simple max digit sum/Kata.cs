using System.Linq;

public class Solution
{
    private static double DigitSum(long n)
    {
        return n.ToString().Sum(char.GetNumericValue);
    }

    public static long solve(long n)
    {
        long p = 1, ans = n;

        while (n > 0)
        {
            var cur = p * (n - 1) + (p - 1);
            var dsCur = DigitSum(cur);
            var dsAns = DigitSum(ans);

            if (dsCur > dsAns || (dsCur == dsAns && ans < cur))
                ans = cur;

            n /= 10;
            p *= 10;
        }

        return ans;
    }
}