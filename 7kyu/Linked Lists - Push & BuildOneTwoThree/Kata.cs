public class Node
{
    public int Data;
    public Node Next;

    public Node(int data)
    {
        Data = data;
        Next = null;
    }

    public static Node Push(Node head, int data) => new Node(data) {Next = head};

    /*
    public static Node BuildOneTwoThree()
    {
        var head = new Node(3);
        head = Node.Push(head, 2);
        head = Node.Push(head, 1);
        
        return head;
    }
*/
    public static Node BuildOneTwoThree() => Push(Push(Push(null, 3), 2), 1);
}