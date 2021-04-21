/*using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;

public static class SortingTask
{
    public static IEnumerable<string> OrderByDomain(this IEnumerable<string> source)
    {
        var domainOrder = new Dictionary<string, int> {["com"] = 1, ["gov"] = 2, ["org"] = 3};
        var uriPattern = @"https?://([a-z0-9]+).([a-z0-9-]+).(?<TLD>[a-z]+)";

        return from site in source
            orderby domainOrder.GetValueOrDefault(
                    Regex.Match(site, uriPattern).Groups["TLD"].Value, 10),
                Regex.Match(site, uriPattern).Groups["TLD"].Value
            select site;
    }
}*/

using System.Collections.Generic;
using System.Linq;

public static class SortingTask
{
    public static IEnumerable<string> OrderByDomain(this IEnumerable<string> source)
    {
        var domainOrder = new Dictionary<string, int> {["com"] = 1, ["gov"] = 2, ["org"] = 3};

        return from url in source
            orderby domainOrder.GetValueOrDefault(
                    new System.Uri(url).Host.Split('.').Last(), 10),
                new System.Uri(url).Host.Split('.').Last()
            select url;
    }
}