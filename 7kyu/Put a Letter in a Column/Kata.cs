/*using System.Linq;

public class Kata
{
    public static string BuildRowText(int index, char character)
    {
        var arr = Enumerable.Repeat(" |", 9).ToArray();
        arr[index] = character + "|";

        return "|" + string.Concat(arr);
    }
}*/

using System.Linq;

public class Kata
{
    public static string BuildRowText(int index, char character)
    {
        return "|" + string.Concat(Enumerable.Range(0, 9).Select(i => $"{(i == index ? character : ' ')}|"));
    }
}