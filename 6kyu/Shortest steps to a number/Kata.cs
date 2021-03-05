/*public static class Kata
{
    public static int ShortestStepsToNum(int num)
    {
        int steps = 0;

        while (num > 1)
        {
            num = (num % 2 == 0 ? num / 2 : num - 1);
            steps++;
        }

        return steps;
    }
}*/

public static class Kata
{
    public static int ShortestStepsToNum(int num)
    {
        return num < 2 ? 0 : 1 + ShortestStepsToNum(num % 2 == 0 ? num / 2 : num - 1);
    }
}