/*public class Line
{
    public static string WhoIsNext(string[] names, long n)
    {
        while (n > names.Length)
            n = (n - names.Length + 1) / 2;

        return names[n - 1];
    }
}*/

public class Line
{
    public static string WhoIsNext(string[] names, long n)
    {
        return n > names.Length ? WhoIsNext(names, (n - names.Length + 1) / 2) : names[n - 1];
    }
}