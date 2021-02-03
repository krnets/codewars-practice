using System.Linq;

public static class Kata
{
    public static string Babel(int height)
    {
        return string.Join('\n', Enumerable.Range(0, height)
            .Select(i => new string(' ', height - i - 1) + new string('o', 2 * i + 1))
            .SelectMany(x => Enumerable.Repeat(x, 3)));
    }
}