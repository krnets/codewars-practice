using System.Linq;

class Kata
{
    public static bool matchingPlates(char[] meals, char[] stack)
    {
        return meals.SequenceEqual(stack.Take(meals.Length));
    }
}