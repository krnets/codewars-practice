using System.Linq;
using System.Text.RegularExpressions;

public class Dinglemouse
{
    public static int CountDeafRats(string town)
    {
        var rat = new Regex("[~O]{2}");
        var split = town.Split("P");
        var deafRatsOnLeft = rat.Matches(split[0]).Count(m => m.Value.Equals("O~"));
        var deafRatsOnRight = rat.Matches(split[1]).Count(m => m.Value.Equals("~O"));

        return deafRatsOnLeft + deafRatsOnRight;
    }
}