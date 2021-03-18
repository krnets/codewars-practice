/*        (1) -> (2) -> (3) -> null
  null <- (1) <- (2) <- (3)       */

/*
public class Kata
{
    public static Node ReverseList(Node node)
    {
        Node prevNode = null;
        Node currNode = node;

        while (currNode != null)
        {
            var nextNode = currNode.Next;
            currNode.Next = prevNode;
            prevNode = currNode;
            currNode = nextNode;
        }

        return prevNode;
    }
}
*/

public class Kata
{
    public static Node ReverseList(Node node)
    {
        Node prevNode = null, currNode = node, nextNode = null;

        while (currNode != null)
        {
            nextNode = currNode.Next;
            currNode.Next = prevNode;
            prevNode = currNode;
            currNode = nextNode;
        }

        return prevNode;
    }
}

/*  stack overflow for large values - not recommended solution

public class Kata
{
    public static Node ReverseList(Node node, Node prev = null)
    {
        return node == null ? prev : ReverseList(node.Next, new Node(node.Value, prev));
    }
}
*/

/* not the most efficient solution due to instantiation of new node on every iteration
 
public class Kata
{
    public static Node ReverseList(Node node)
    {
        Node head = null;

        while (node != null)
        {
            head = new Node(node.Value, head);
            node = node.Next;
        }

        return head;
    }
}*/