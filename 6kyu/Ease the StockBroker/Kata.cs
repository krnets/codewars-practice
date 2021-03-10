using System;
using System.Collections.Generic;
using System.Text.RegularExpressions;
using static System.String;

public class OrdersSummary
{
    public static string balanceStatements(string lst)
    {
        double bought = 0, sold = 0;
        var typos = new List<string>();
        var pattern = @"^.*?(\d+) (\d*\.\d+) ([BS])$";

        foreach (var order in lst.Split(", "))
        {
            if (Regex.IsMatch(order, pattern))
            {
                var simple = order.Split();
                var totalPrice = int.Parse(simple[1]) * double.Parse(simple[2]);

                if (simple[3].Equals("B"))
                    bought += totalPrice;
                else sold += totalPrice;
            }
            else typos.Add($"{order} ;");
        }

        return $"Buy: {Math.Round(bought)} Sell: {Math.Round(sold)}" +
               $"{(typos.Count == 0 || lst.Length == 0 ? Empty : $"; Badly formed {typos.Count}: {Join("", typos)}")}";
    }
}