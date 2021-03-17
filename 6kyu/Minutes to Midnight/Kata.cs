using System;

public class Minute
{
    public string countMinutes(DateTime d)
    {
        // var diff = Math.Round((DateTime.Today.AddDays(1) - d).TotalMinutes);
        var diff = Math.Round((d.Date.AddDays(1) - d).TotalMinutes);

        return $"{diff} minute{(diff > 1 ? "s" : "")}";
    }
}