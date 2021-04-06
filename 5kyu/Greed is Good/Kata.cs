public static class Kata
{
    public static int Score(int[] dice)
    {
        var countDice = new int[7];

        foreach (int x in dice)
            countDice[x]++;

        return (countDice[1] / 3 * 1000) + (countDice[1] % 3 * 100) +
               (countDice[2] / 3 * 200) +
               (countDice[3] / 3 * 300) +
               (countDice[4] / 3 * 400) +
               (countDice[5] / 3 * 500) + (countDice[5] % 3 * 50) +
               (countDice[6] / 3 * 600);
    }
}