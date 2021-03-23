using System.Linq;

public class IntroToArt
{
    public string[] GetW(int h)
    {
        if (h < 2) return new string[] { };

        var result = new char[h][];
        var length = h + 3 * (h - 1);

        for (int i = 0; i < h; i++)
            result[i] = Enumerable.Repeat(' ', length).ToArray();

        var forward = Enumerable.Range(0, h).ToArray();
        var reverse = forward.SkipLast(1).Reverse().ToArray();
        var positions = forward.Concat(reverse).Concat(forward.Skip(1)).Concat(reverse).ToArray();

        for (int j = 0; j < length; j++)
        {
            var pos = positions[j];
            result[pos][j] = '*';
        }

        return result.Select(row => string.Concat(row)).ToArray();
    }
}