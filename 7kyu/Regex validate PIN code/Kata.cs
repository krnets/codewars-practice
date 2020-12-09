using System.Linq;
using System.Text.RegularExpressions;

public class Kata
{
    public static bool ValidatePin(string pin)
    {
        // return Regex.IsMatch(pin, @"^(\d{4}|\d{6})\z");
        return (pin.Length == 4 || pin.Length == 6) && pin.All(char.IsDigit);
    }
}