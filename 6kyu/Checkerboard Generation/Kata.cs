/*using System.Text;

public static class Kata
{
    public static string Checkerboard(int size)
    {
        var sb = new StringBuilder();

        for (int i = 0; i < size; i++)
        {
            for (int j = 0; j < size; j++)
                if (i % 2 == 0)
                    sb.Append(j % 2 == 0 ? "[r]" : "[b]");
                else
                    sb.Append(j % 2 == 0 ? "[b]" : "[r]");

            sb.Append("\n");
        }

        return sb.ToString();
    }
}*/

/*using System;
using System.Linq;
using System.Text;

public static class Kata
{
    public static string Checkerboard(int size)
    {
        if (size <= 0)
            return string.Empty;

        var arr = new string[size];

        for (int i = 0; i < Math.Min(2, size); i++)
        {
            var sb = new StringBuilder();

            for (int j = 0; j < size; j++)
            {
                if (i % 2 == 0)
                    sb.Append(j % 2 == 0 ? "[r]" : "[b]");
                else sb.Append(j % 2 == 0 ? "[b]" : "[r]");
            }

            arr[i] = sb.Append("\n").ToString();
        }

        return string.Concat(Enumerable.Range(0, size).Select(i => arr[i % 2]));
    }
}*/

using System;
using System.Linq;
using System.Text;

public static class Kata
{
    public static string Checkerboard(int size)
    {
        if (size <= 0) return string.Empty;
        var arr = new string[2];

        for (int i = 0; i < Math.Min(2, size); i++)
        {
            var sb = new StringBuilder();

            for (int j = 0; j < size; j++)
                sb.Append((i + j) % 2 == 0 ? "[r]" : "[b]");

            arr[i] = $"{sb}\n";
        }

        return string.Concat(Enumerable.Range(0, size).Select(i => arr[i % 2]));
    }
}