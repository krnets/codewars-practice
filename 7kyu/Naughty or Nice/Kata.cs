using System.Collections.Generic;
using System.Linq;

public class NaughtyOrNice
{
    public static IEnumerable<string> GetNiceNames(IEnumerable<Person> people)
    {
        return people.Where(p => p.WasNice).Select(p => p.Name);
    }

    public static IEnumerable<string> GetNaughtyNames(IEnumerable<Person> people)
    {
        return people.Where(p => !p.WasNice).Select(p => p.Name);
    }
}

class Person
{
    public string Name { get; set; }
    public bool WasNice { get; set; }
}