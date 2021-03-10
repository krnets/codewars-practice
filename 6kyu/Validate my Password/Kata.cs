using System.Text.RegularExpressions;

public class validPass
{
    public static string validator(string password)
    {
        var rules = @"^(?=.*[A-Za-z])(?=.*\d)\w{4,19}$";

        return $"{(Regex.IsMatch(password, rules) ? "" : "IN")}VALID";
    }
}