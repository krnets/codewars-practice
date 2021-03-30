using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;

public class TitleSorter
{
    public List<string> Sort(List<string> unsortedTitles)
    {
        return unsortedTitles?
            .OrderBy(s => Regex.Replace(s, @"^(an?|the)\s(.+)$", "$2, $1", RegexOptions.IgnoreCase))
            .ToList();
    }
}