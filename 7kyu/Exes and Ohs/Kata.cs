public static class Kata
{
    public static bool XO(string input)
    {
        int countXs = 0;
        int countOs = 0;

        foreach (var c in input.ToLower())
            switch (c)
            {
                case 'x': countXs++; break;
                case 'o': countOs++; break;
            }

        return countXs == countOs;
    }
}