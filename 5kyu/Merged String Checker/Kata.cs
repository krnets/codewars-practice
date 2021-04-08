public class StringMerger
{
    public static bool isMerge(string s, string part1, string part2)
    {
        if (!string.IsNullOrEmpty(s) && part1 == part2 || (part1.Length + part2.Length) != s.Length)
            return false;

        int i = 0, j = 0;

        foreach (char c in s)
        {
            if (i < part1.Length && part1[i] == c) i++;
            if (j < part2.Length && part2[j] == c) j++;
        }

        return i + j == s.Length;
    }
}