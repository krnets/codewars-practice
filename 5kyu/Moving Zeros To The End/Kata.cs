/*using System.Linq;

public class Kata
{
    public static int[] MoveZeroes(int[] arr)
    {
        return arr.Where(x => x != 0).Concat(arr.Where(x => x == 0)).ToArray();
    }
}*/

/*using System.Linq;

public class Kata
{
    public static int[] MoveZeroes(int[] arr)
    {
        return arr.OrderBy(x => x == 0).ToArray();
    }
}*/

public class Kata
{
    public static int[] MoveZeroes(int[] arr)
    {
        var zeroFound = false;
        int zeroIndex = -1;

        for (int i = 0; i < arr.Length; i++)
        {
            if (arr[i] == 0 && !zeroFound)
            {
                zeroFound = true;
                zeroIndex = i;
            }

            else if (arr[i] != 0 && zeroFound)
            {
                (arr[i], arr[zeroIndex]) = (arr[zeroIndex], arr[i]);
                zeroIndex++;
            }
        }

        return arr;
    }
}