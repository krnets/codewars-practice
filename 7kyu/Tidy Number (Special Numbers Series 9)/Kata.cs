using System.Linq;

class Kata
{
    public static bool TidyNumber(int n)
    {
        var list = n.ToString().Select(char.GetNumericValue).ToList();

        // return list.Zip(list.Skip(1)).All(tuple => tuple.Second - tuple.First >= 0);
        return list.Zip(list.Skip(1)).All(t => t.First <= t.Second);
    }
}


/*
using System.Linq;

class Kata
{
    public static bool TidyNumber(int n)
    {
        return n == int.Parse(string.Concat(n.ToString().OrderBy(c => c)));
    }
}
*/

/*using System.Linq;

class Kata
{
    public static bool TidyNumber(int n)
    {
        return n.ToString()
            .Skip(1)
            .Zip(n.ToString(), (b, a) => new[] {a - '0', b - '0'})
            .All(x => x[0] <= x[1]);
    }
}*/