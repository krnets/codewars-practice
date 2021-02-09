/*using System.Linq;

public class Kata
{
    public static int FindNumber(int[] array)
    {
        return array.Length == 0 ? 1 : Enumerable.Range(1, array.Max() + 1).Except(array).First();
    }
}*/

/*using System.Linq;

public class Kata
{
    public static int FindNumber(int[] array) => Enumerable.Range(1, array.Length + 1).Except(array).Single();
}*/

using System.Linq;

public class Kata
{
    public static int FindNumber(int[] array)
    {
        int length = array.Length;

        return (length + 1) * (length + 2) / 2 - array.Sum();
    }
}