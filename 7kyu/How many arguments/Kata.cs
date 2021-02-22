/*public static class Kata
{
    public static int CountArgs(params object[] argObjects)
    {
        return argObjects.Length;
    }
}*/

public static class Kata
{
    public static int CountArgs(params dynamic[] args)
    {
        return args.Length;
    }
}