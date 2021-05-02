using System.Collections.Generic;

class Kata
{
    public static List<int> TreeByLevels(Node node)
    {
        var list = new List<int>();
        var queue = new Queue<Node>();

        if (node != null)
            queue.Enqueue(node);

        while (queue.Count > 0)
        {
            var currNode = queue.Dequeue();

            list.Add(currNode.Value);

            if (currNode.Left != null) queue.Enqueue(currNode.Left);
            if (currNode.Right != null) queue.Enqueue(currNode.Right);
        }

        return list;
    }
}

/*using System.Collections.Generic;
using System.Linq;

class Kata
{
    public static List<int> TreeByLevels(Node node)
    {
        var list = new List<Node>();

        if (node != null)
            list.Add(node);

        for (int i = 0; i < list.Count; i++)
        {
            if (list[i].Left != null) list.Add(list[i].Left);
            if (list[i].Right != null) list.Add(list[i].Right);
        }

        return list.Select(x => x.Value).ToList();
    }
}*/