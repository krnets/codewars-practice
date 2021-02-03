using System.Linq;

class Kata
{
    public static string SpecialNumber(int number)
    {
        return number.ToString().All(x => char.GetNumericValue(x) <= 5) ? "Special!!" : "NOT!!";
    }
}