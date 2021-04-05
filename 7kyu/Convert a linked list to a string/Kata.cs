/*using System.Collections.Generic;

public class Kata
{
    public static string Stringify(Node list)
    {
        var result = new List<string>();

        while (list != null)
        {
            result.Add(list.Data.ToString());
            list = list.Next;
        }

        result.Add("null");

        return string.Join(" -> ", result);
    }
}*/

/*
public class Kata
{
    public static string Stringify(Node list)
    {
        // return list != null ? list.Data + " -> " + Stringify(list.Next) : "null";
        // return list == null ? "null" : $"{list.Data} -> {Stringify(list.Next)}";
        return list == null ? "null" : list.Data + " -> " + Stringify(list.Next);
    }
}
*/

/*using System.Text;

public class Kata
{
    public static string Stringify(Node list)
    {
        var sb = new StringBuilder();

        while (list != null)
        {
            sb.Append($"{list.Data} -> ");
            list = list.Next;
        }

        return $"{sb}null";
    }
}*/

/*using System.Text;

public class Kata
{
    public static string Stringify(Node list)
    {
        var sb = new StringBuilder();

        while (list != null)
        {
            sb.Append($"{list.Data} -> ");
            list = list.Next;
        }

        return $"{sb}null";
    }
}*/

using System.Collections.Generic;

public class Kata
{
    public static string Stringify(Node list)
    {
        return string.Join(" -> ", Adapt(list));
    }

    private static IEnumerable<string> Adapt(Node list)
    {
        while (list != null)
        {
            yield return list.Data.ToString();
            list = list.Next;
        }

        yield return "null";
    }
}