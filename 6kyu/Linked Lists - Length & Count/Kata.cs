using System;

public partial class Node
{
    public int Data;
    public Node Next;

    public Node(int data) => Data = data;

    // public static int Length(Node head) =>  
    //     head == null ? 0 : 1 + Length(head.Next);
    public static int Length(Node head) => Count(head, _ => true);

    public static int Count(Node head, Predicate<int> func) =>
        head == null ? 0 : (func.Invoke(head.Data) ? 1 : 0) + Count(head.Next, func);
    /*
    public static int Length(Node head)
    {
        int counter = 0;

        while (head != null)
        {
            head = head.Next;
            counter++;
        }

        return counter;
    }

    public static int Count(Node head, Predicate<int> func)
    {
        int counter = 0;

        while (head != null)
        {
            if (func.Invoke(head.Data))
                counter++;

            head = head.Next;
        }

        return counter;
    }
    */

    public static Node Push(Node head, int data) => new Node(data) {Next = head};

    public static Node BuildOneTwoThree() => Push(Push(Push(null, 3), 2), 1);
}