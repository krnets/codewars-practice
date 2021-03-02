/*public class Kata
{
    private static bool _flag;

    public static bool omnibool
    {
        get => _flag = !_flag;
        set => _flag = value;
    }
}*/

public class Kata
{
    private static bool x;

    public static bool omnibool => x = !x;
}