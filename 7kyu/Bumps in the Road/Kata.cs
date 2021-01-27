using System.Linq;

class Kata
{
    public static string Bump(string input)
    {
        return input.Count(c => c == 'n') <= 15 ? "Woohoo!" : "Car Dead";
        //return input.Trim('n').Length > 15 ? "Car Dead" : "Woohoo!";
    }
}