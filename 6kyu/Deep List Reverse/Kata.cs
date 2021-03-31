using System.Linq;

public class Kata
{
    public static object[] DeepReverse(object[] l)
    {
        return l.Select(o => o.GetType().IsArray ? DeepReverse((object[]) o) : o).Reverse().ToArray();
    }
}