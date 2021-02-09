/*using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;

public static class Kata
{
    public static string GetOrder(string input)
    {
        var order = new List<string>();
        var menu = new[] {"Burger", "Fries", "Chicken", "Pizza", "Sandwich", "Onionrings", "Milkshake", "Coke"};
        var map = Regex.Matches(input, string.Join("|", menu), RegexOptions.IgnoreCase)
            .GroupBy(m => m.Value)
            .ToDictionary(g => g.Key, g => g.Count());

        foreach (var item in menu)
        {
            var itemLower = item.ToLower();

            if (map.ContainsKey(itemLower))
                while (map[itemLower] > 0)
                {
                    order.Add(item);
                    map[itemLower]--;
                }
        }

        return string.Join(" ", order);
    }
}*/

using System.Collections.Generic;
using System.Globalization;
using System.Linq;
using System.Text.RegularExpressions;

public static class Kata
{
    public static string GetOrder(string input)
    {
        var menu = new List<string> {"Burger", "Fries", "Chicken", "Pizza", "Sandwich", "Onionrings", "Milkshake", "Coke"};
        var ti = CultureInfo.CurrentCulture.TextInfo;

        return string.Join(" ", Regex.Matches(input, string.Join("|", menu), RegexOptions.IgnoreCase)
            .Select(m => ti.ToTitleCase(m.Value))
            .OrderBy(item => menu.IndexOf(item)));
    }
}