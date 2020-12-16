using System.Linq;

public class Kata
{
    public static int FindEvenIndex(int[] arr)
    {
        int leftSum = 0;
        int rightSum = arr.Sum();

        for (int i = 0; i < arr.Length; i++)
        {
            rightSum -= arr[i];

            if (leftSum == rightSum)
                return i;

            leftSum += arr[i];
        }

        return -1;
    }
}

/*using System.Linq;

public class Kata
{
    public static int FindEvenIndex(int[] arr)
    {
        return Enumerable.Range(0, arr.Length).ToList().FindIndex(i => arr[..i].Sum() == arr[(i + 1)..].Sum());
    }
}*/