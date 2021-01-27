using System.Linq;

static class Kata
{
    public static bool vampire_test(long x, long y)
    {
        return $"{x}{y}".OrderBy(c => c).SequenceEqual($"{x * y}".OrderBy(c => c));
    }
}