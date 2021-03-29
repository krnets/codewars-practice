/*using System;
using System.Collections.Generic;
using System.Linq;

public static class Kata
{
    public static IEnumerable<IEnumerable<object>> GroupWhile(this IEnumerable<object> coll, Func<object, bool> pred)
    {
        var listOfLists = new List<List<object>>();
        var previous = coll.First();
        var list = new List<object> {previous};

        foreach (var item in coll.Skip(1))
        {
            if (pred(item) != pred(previous) || pred(previous) == false)
            {
                listOfLists.Add(list);
                list = new List<object>();
            }

            list.Add(item);
            previous = item;
        }

        listOfLists.Add(list);

        return listOfLists;
    }
}*/

using System;
using System.Collections.Generic;
using System.Linq;

public static class Kata
{
    public static IEnumerable<IEnumerable<object>> GroupWhile(this IEnumerable<object> coll, Func<object, bool> pred)
    {
        List<object> list = new List<object> {coll.First()};

        foreach (object item in coll.Skip(1))
        {
            if (pred(item) == false || pred(list.Last()) == false)
            {
                yield return list;
                list = new List<object>();
            }

            list.Add(item);
        }

        yield return list;
    }
}