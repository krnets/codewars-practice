/*using static System.Linq.Enumerable;

public class PaddedNumbers
{
    public static string Solution(int value)
    {
        return $"Value is {string.Concat(Repeat('0', 5 - value.ToString().Length))}{value}";
    }
}*/

public class PaddedNumbers
{
    public static string Solution(int value)
    {
        return $"Value is {value:D5}";
    }
}

/*public class PaddedNumbers
{
    public static string Solution(int value)
    {
        return "Value is " + value.ToString().PadLeft(5, '0');
    }
}*/