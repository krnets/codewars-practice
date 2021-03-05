using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;

class HtmlColorParser
{
    private readonly IDictionary<string, string> presetColors;

    public HtmlColorParser(IDictionary<string, string> presetColors)
    {
        this.presetColors = presetColors;
    }

    public RGB Parse(string color)
    {
        if (!color.Contains('#'))
            return Parse(presetColors[color.ToLower()]);

        var bytes = Regex.Split(color[1..], @"(?<=\G.{" + color.Length / 3 + "})")
            .Take(3)
            .Select(hex => Convert.ToByte((hex.Length == 2 ? hex : hex + hex), 16))
            .ToArray();

        return new RGB(bytes[0], bytes[1], bytes[2]);
    }
}