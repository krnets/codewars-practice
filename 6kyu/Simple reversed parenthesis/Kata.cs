public class Solution
{
    public static int solve(string s)
    {
        if (s.Length % 2 != 0) return -1;

        int count = 0;

        while (s.Contains("()"))
            s = s.Replace("()", "");

        for (int i = 1; i < s.Length; i += 2)
            if (s[i - 1] == s[i])
                count++;
            else count += 2;

        return count;
    }
}