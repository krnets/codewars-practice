/*public class Kata
{
    public static object[] Rotate(object[] array, int n)
    {
        var result = new object[array.Length];
        n = n < 0 ? array.Length + (n % array.Length) : n;

        for (int i = 0; i < array.Length; i++)
            result[(i + n) % array.Length] = array[i];

        return result;
    }
}*/

using System.Linq;

public class Kata
{
    public static object[] Rotate(object[] array, int n)
    {
        int pos = (array.Length - (n % array.Length)) % array.Length;

        return array.Skip(pos).Concat(array.Take(pos)).ToArray();
    }
}