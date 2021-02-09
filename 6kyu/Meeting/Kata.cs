using System.Linq;

public class JohnMeeting
{
    public static string Meeting(string s)
    {
        return string.Concat(s.ToUpper().Split(';')
            .Select(name => name.Split(':'))
            .Select(name => $"({name[1]}, {name[0]})")
            .OrderBy(x => x));
    }
}