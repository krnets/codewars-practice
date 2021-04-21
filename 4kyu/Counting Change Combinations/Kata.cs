public static class Kata
{
    public static int CountCombinations(int money, int[] coins)
    {
        var ways = new int[money + 1];
        ways[0] = 1;

        foreach (int coin in coins)
            for (int i = 1; i <= money; i++)
                if (i >= coin)
                    ways[i] += ways[i - coin];

        return ways[money];
    }
}