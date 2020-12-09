using System.Collections.Generic;
using System.Linq;

public class ListFilterer
{
    public static IEnumerable<int> GetIntegersFromList(List<object> listOfItems)
    {
        // var list = new List<int>();
        //
        // foreach (var item in listOfItems)
        //     if (item is int)
        //         list.Add((int) item);
        //
        // return list;

        foreach (var item in listOfItems)
            if (item is int)
                yield return (int) item;

        // return listOfItems.Where(item => item.GetType() == 1.GetType()).Cast<int>();
        // return listOfItems.Where(x => x is int).Cast<int>();
        // return listOfItems.OfType<int>();
    }
}