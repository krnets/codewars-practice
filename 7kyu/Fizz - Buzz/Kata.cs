/*using System.Linq;

public class Kata
{
    public static int[] Solution(int number)
    {
        var seq = Enumerable.Range(1, number - 1);
        var A = seq.Count(x => x % 3 == 0 && x % 5 != 0);
        var B = seq.Count(x => x % 3 != 0 && x % 5 == 0);
        var C = seq.Count(x => x % 3 == 0 && x % 5 == 0);

        return new[] {A, B, C};
    }
}*/

public class Kata
{
    public static int[] Solution(int number)
    {
        var a = (number - 1) / 3;
        var b = (number - 1) / 5;
        var c = (number - 1) / (3 * 5);

        return new[] {a - c, b - c, c};
    }
}