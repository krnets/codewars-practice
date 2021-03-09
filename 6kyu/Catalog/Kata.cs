/*using System.Collections.Generic;
using System.Linq;

public class Catalogue
{
    public static string Catalog(string s, string article)
    {
        var linesWithArticle = s.Split("\n\n").Where(line => line.Contains(article)).ToArray();
        var linesFormatted = new List<string>();
        string nameTag = "<name>", nameTagClose = "</name>";
        string prxTag = "<prx>", prxTagClose = "</prx>";
        string qtyTag = "<qty>", qtyTagClose = "</qty>";

        foreach (var line in linesWithArticle)
        {
            var name = line[(line.IndexOf(nameTag) + nameTag.Length)..(line.IndexOf(nameTagClose))];
            var price = line[(line.IndexOf(prxTag) + prxTag.Length)..(line.IndexOf(prxTagClose))];
            var quantity = line[(line.IndexOf(qtyTag) + qtyTag.Length)..(line.IndexOf(qtyTagClose))];

            linesFormatted.Add($"{name} > prx: ${price} qty: {quantity}");
        }

        return linesFormatted.Count == 0 ? "Nothing" : string.Join("\n", linesFormatted);
    }
}*/

using System.Linq;

public class Catalogue
{
    public static string Catalog(string s, string article)
    {
        string nameTag = "<name>", prxTag = "<prx>", qtyTag = "<qty>";

        var linesFormatted = (from line in s.Split("\n\n").Where(line => line.Contains(article))
            let name = line[(line.IndexOf(nameTag) + nameTag.Length)..(line.IndexOf(nameTag.Insert(1, "/")))]
            let price = line[(line.IndexOf(prxTag) + prxTag.Length)..(line.IndexOf(prxTag.Insert(1, "/")))]
            let quantity = line[(line.IndexOf(qtyTag) + qtyTag.Length)..(line.IndexOf(qtyTag.Insert(1, "/")))]
            select $"{name} > prx: ${price} qty: {quantity}").ToList();

        return linesFormatted.Count == 0 ? "Nothing" : string.Join("\n", linesFormatted);
    }
}