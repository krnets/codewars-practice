/*
using System.Linq;

public class Kata
{
    public static int FindTheKey(string message, int[] code)
    {
        var keyCycle = code.Zip(message, (f, s) => f - (s - 'a') - 1).ToArray();

        for (int i = 1; i <= keyCycle.Length; i++)
            if (keyCycle.Select((v, idx) => v == keyCycle[idx % i]).All(x => x))
                return int.Parse(string.Concat(keyCycle[..i]));

        return -1;
    }
}
*/

using System.Linq;

public class Kata
{
    public static int FindTheKey(string message, int[] code)
    {
        var keyCycle = message.Zip(code, (f, s) => s - (f - 'a') - 1).ToArray();

        return Enumerable.Range(1, keyCycle.Length)
            .Where(i => keyCycle.Select((v, idx) => v == keyCycle[idx % i]).All(x => x))
            .Select(i => int.Parse(string.Concat(keyCycle[..i])))
            .FirstOrDefault();
    }
}