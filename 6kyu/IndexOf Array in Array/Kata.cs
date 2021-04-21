/*using System;
using System.Linq;

public class Kata
{
    public static int SearchArray(object[][] arrayToSearch, object[] query)
    {
        if (arrayToSearch.Any(x => x.Length != 2) || query.Length != 2) throw new Exception();

        var cmp = string.Concat(query);

        for (int i = 0; i < arrayToSearch.Length; i++)
            if (string.Concat(arrayToSearch[i]) == cmp)
                return i;

        return -1;
    }
}*/

/*using System;
using System.Linq;

public class Kata
{
    public static int SearchArray(object[][] arrayToSearch, object[] query)
    {
        if (arrayToSearch.Any(x => x.Length != query.Length)) throw new Exception();

        for (int i = 0; i < arrayToSearch.Length; i++)
            if (arrayToSearch[i].SequenceEqual(query))
                return i;

        return -1;
    }
}*/

using System;
using System.Linq;

public class Kata
{
    public static int SearchArray(object[][] arrayToSearch, object[] query)
    {
        if (arrayToSearch.Any(x => !x.GetType().IsArray || x.Length != 2) || query.Length != 2) throw new Exception();

        return arrayToSearch.ToList().FindIndex(x => x.SequenceEqual(query));
    }
}