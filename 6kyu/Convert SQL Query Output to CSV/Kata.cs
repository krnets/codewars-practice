using System.Linq;
using static System.String;

public class SqlQueryOutputToCsvConverter
{
    public string Convert(string[] lines)
    {
        return Concat(lines.Take(1).Concat(lines.Skip(2).SkipLast(2))
            .Select(line => Join(",", line[..^2].Split(",")
                .Select(str => str.Trim().Replace("NULL", ""))) + "\r\n"));
    }
}