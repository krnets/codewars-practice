/*using System;
using System.Text.RegularExpressions;

public class Printer
{
    public static string PrinterError(String s)
    {
        int errors = 0;

        foreach (char c in s)
            if (Regex.IsMatch(c + "", "[^a-m]"))
                errors++;

        return $"{errors}/{s.Length}";
    }
}*/

/*using System;
using System.Linq;

public class Printer
{
    public static string PrinterError(String s)
    {
        return $"{s.Count(c => c > 'm')}/{s.Length}";
    }
}*/

/*using System;
using System.Text.RegularExpressions;

public class Printer
{
    public static string PrinterError(String s)
    {
        string pattern = "[^a-m]";
        
        return $"{Regex.Matches(s, pattern).Count}/{s.Length}";
    }
}*/

using System;
using System.Linq;

public class Printer
{
    public static string PrinterError(String s)
    {
        return s.Count(c => c > 'm') + "/" + s.Length;
    }
}