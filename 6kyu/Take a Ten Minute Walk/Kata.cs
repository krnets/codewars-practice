public class Kata
{
    public static bool IsValidWalk(string[] walk)
    {
        if (walk.Length != 10) return false;

        int x = 0, y = 0;

        foreach (var direction in walk)
            switch (direction)
            {
                case "n": y++; break;
                case "s": y--; break;
                case "e": x++; break;
                case "w": x--; break;
            }

        return x == 0 && y == 0;
    }
}