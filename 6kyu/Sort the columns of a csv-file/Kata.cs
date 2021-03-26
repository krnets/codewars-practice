/*using System.Linq;

public class Kata
{
    public static string SortCsvColumns(string csvFileContent)
    {
        var rows = csvFileContent.Split("\n");
        var nRows = rows.Length;
        var table = rows.Select(row => row.Split(";").ToArray()).ToArray();
        var nColumns = table[0].Length;
        var sortedNames = table[0].OrderBy(name => name.ToLower()).ToList();
        var sortedIndex = table[0].Select(str => sortedNames.IndexOf(str)).ToArray();
        var result = new string[nRows][];

        for (int i = 0; i < nRows; i++)
        {
            result[i] = new string[nColumns];

            for (int j = 0; j < nColumns; j++)
                result[i][sortedIndex[j]] = table[i][j];
        }

        return string.Join("\n", result.Select(row => string.Join(";", row)));
    }
}*/

using System.Linq;

public class Kata
{
    public static string SortCsvColumns(string csvFileContent)
    {
        var table = csvFileContent.Split("\n").Select(line => line.Split(";")).ToArray();

        var indices = table[0].Select((s, i) => new {Value = s, Index = i})
            .OrderBy(x => x.Value)
            .Select(x => x.Index)
            .ToArray();

        return string.Join("\n", table.Select(line => string.Join(";", indices.Select(i => line[i]))));
    }
}

/*using System.Linq;

public class Kata
{
    public static string SortCsvColumns(string csvFileContent)
    {
        var lines = csvFileContent.Split("\n").Select(a => a.Split(';')).ToArray();

        for (int i = 0; i < lines[0].Length; i++)
        {
            for (int j = 0; j < lines[0].Length - 1; j++)
            {
                if (lines[0][j].CompareTo(lines[0][j + 1]) > 0)
                    foreach (var line in lines)
                        (line[j], line[j + 1]) = (line[j + 1], line[j]);
            }
        }

        return string.Join("\n", lines.Select(line => string.Join(";", line)));
    }
}*/