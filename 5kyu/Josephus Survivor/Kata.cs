using System.Linq;

public class JosephusSurvivor
{
    public static int JosSurvivor(int n, int k)
    {
        var list = Enumerable.Range(1, n).ToList();
        int i = 0;

        while (list.Count > 1)
        {
            i = (i + k - 1) % list.Count;
            list.RemoveAt(i);
        }

        return list.First();
    }
}