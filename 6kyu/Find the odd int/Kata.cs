/*class Kata
{
    public static int find_it(int[] seq)
    {
        int xor = 0;

        foreach (int x in seq)
            xor ^= x;

        return xor;
    }
}*/


/*using System.Linq;

class Kata
{
    public static int find_it(int[] seq)
    {
        return seq.First(x => seq.Count(y => y == x) % 2 == 1);
    }
}*/

using System.Linq;

class Kata
{
    public static int find_it(int[] seq)
    {
        return seq.GroupBy(x => x).Single(g => g.Count() % 2 == 1).Key;
    }
}