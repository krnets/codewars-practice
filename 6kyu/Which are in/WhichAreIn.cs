/*using System.Linq;

class WhichAreIn
{
    public static string[] inArray(string[] array1, string[] array2)
    {
        return array1
            .Where(x => array2.Any(y => y.Contains(x)))
            .Distinct()
            .OrderBy(s => s)
            .ToArray();
    }
}*/

using System.Linq;

class WhichAreIn
{
    public static string[] inArray(string[] array1, string[] array2)
    {
        return array1.Distinct()
            .Where(x => array2.Any(y => y.Contains(x)))
            .OrderBy(s => s)
            .ToArray();
    }
}