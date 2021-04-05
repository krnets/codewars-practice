using System;
using System.Collections.Generic;

public class Node
{
    public int Data;
    public Node Next;

    public Node(int data, Node next = null)
    {
        Data = data;
        Next = next;
    }

    public override bool Equals(Object obj)
    {
        if (obj == null || GetType() != obj.GetType())
            return false;

        return ToString() == obj.ToString();
    }

    public override string ToString()
    {
        List<int> result = new List<int>();
        Node current = this;

        while (current != null)
        {
            result.Add(current.Data);
            current = current.Next;
        }

        return string.Join(" -> ", result) + " -> null";
    }
}