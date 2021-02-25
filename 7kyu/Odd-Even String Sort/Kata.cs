using System.Text;

public class Kata
{
    public static string SortMyString(string s)
    {
        var odd = new StringBuilder();
        var even = new StringBuilder();

        for (int i = 0; i < s.Length; i++)
            if (i % 2 == 0)
                even.Append(s[i]);
            else odd.Append(s[i]);

        return string.Join(" ", even, odd);
    }
}

/*using System.Text;

public class Kata
{
    public static string SortMyString(string s)
    {
        var odd = new StringBuilder();
        var even = new StringBuilder();
        bool toggle = false;

        foreach (char c in s)
            if (toggle = !toggle) even.Append(c);
            else odd.Append(c);

        return string.Join(" ", even, odd);
    }
}*/