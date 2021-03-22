/*using System.Collections.Generic;
using System.Text;

public class Ticker
{
    public static string Interpret(string tape)
    {
        var sb = new StringBuilder();
        var map = new Dictionary<int, int>();

        for (int i = 0, selector = 0; i < tape.Length; i++)
            switch (tape[i])
            {
                case '>':
                    selector++;
                    break;
                case '<':
                    selector--;
                    break;
                case '+':
                    if (!map.ContainsKey(selector)) map[selector] = 1;
                    else map[selector]++;
                    break;
                case '*':
                    sb.Append((char) (map[selector] % 256));
                    break;
            }


        return sb.ToString();
    }
}*/

using System.Collections.Generic;
using System.Linq;
using System.Text;

public class Ticker
{
    public static string Interpret(string tape)
    {
        var sb = new StringBuilder();
        var list = new List<int>(Enumerable.Repeat(0, 34));

        for (int i = 0, selector = 25; i < tape.Length; i++)
            switch (tape[i])
            {
                case '>': selector++; break;
                case '<': selector--; break;
                case '+': list[selector] = (list[selector] == 255 ? 0 : list[selector] + 1); break;
                case '*': sb.Append((char) (list[selector] % 256)); break;
            }

        return sb.ToString();
    }
}