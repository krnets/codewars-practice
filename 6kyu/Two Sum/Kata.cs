public class Kata
{
    public static int[] TwoSum(int[] numbers, int target)
    {
        for (int i = 0; i < numbers.Length; i++)
        for (int j = 1; j < numbers.Length; j++)
            if (numbers[i] + numbers[j] == target)
                return new[] {i, j};

        return new[] {-1, -1};
    }
}