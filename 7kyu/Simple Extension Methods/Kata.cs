static class SimpleExtensions
{
    public static string SayHello(this string name)
    {
        return $"Hello, {name}!";
    }

    public static string SayGoodbye(this string name)
    {
        return $"Goodbye, {name}. See you again soon!";
    }
}