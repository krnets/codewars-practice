/*using System;

public class Kata
{
    public static int RoundToNext5(int n)
    {
        return (int)(Math.Ceiling(n / 5.0) * 5);
    }
}
*/
/*public class Kata
{
    public static int RoundToNext5(int n)
    {
        return n + (5 - n % 5) % 5;
    }
}*/

/*public class Kata
{
    public static int RoundToNext5(int n)
    {
        while (n % 5 != 0) n++;
        return n;
    }
}*/

public class Kata
{
    public static int RoundToNext5(int n) => n % 5 == 0 ? n : RoundToNext5(n + 1);
}