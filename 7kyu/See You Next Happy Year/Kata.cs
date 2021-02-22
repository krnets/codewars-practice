using System.Linq;

public class Kata
{
    public short nextHappyYear(short year)
    {
        var next = year + 1;

        while (next.ToString().Distinct().Count() != 4)
            next++;

        return (short) next;
    }
}

/*using System.Linq;

public class Kata
{
    public short nextHappyYear(short year)
    {
        while ((++year).ToString().Distinct().Count() != 4) { }

        return year;
    }
}*/