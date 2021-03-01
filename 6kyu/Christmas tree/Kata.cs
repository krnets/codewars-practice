/*using System.Collections.Generic;

public class ChristmasTreeGenerator
{
    public static string ChristmasTree(int height)
    {
        var list = new List<string>();

        for (int i = 0; i < height; i++)
        {
            var stars = new string('*', 2 * i + 1);
            var padding = new string(' ', height - stars.Length + i);
            list.Add(padding + stars + padding);
        }

        return string.Join("\n", list);
    }
}*/

using System.Linq;

public class ChristmasTreeGenerator
{
    public static string ChristmasTree(int height)
    {
        return string.Join("\n",
            Enumerable.Range(1, height)
                .Select(i => new string('*', 2 * i - 1).PadLeft(height + i - 1).PadRight(2 * height - 1)));
    }
}