/*public class Kata
{
    public static int FindShort(string s)
    {
        string[] arr = s.Split();
        string shortestElement = arr[0];

        foreach (var str in arr)
            if (str.Length < shortestElement.Length)
                shortestElement = str;

        return shortestElement.Length;
    }
}*/

/*
using System.Linq;

public class Kata
{
    public static int FindShort(string s)
    {
        return s.Split(' ').Select(word => word.Length).Min();
    }
}*/

/*
public class Kata
{
    public static int FindShort(string s)
    {
        var arr = s.Split();
        var shortest = arr.OrderByDescending(w => w.Length).Last();
        return shortest.Length;
    }
}*/

using System.Linq;

public class Kata
{
    public static int FindShort(string s)
    {
        return s.Split(' ').OrderBy(w => w.Length).First().Length;
    }
}